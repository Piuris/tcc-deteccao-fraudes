import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from fraude.config import CostConfig
from fraude.robustness import (
    brier_skill,
    duplicate_effect_fixed_model,
    elkan_threshold,
    final_model_robustness,
    stratified_bootstrap,
)
from fraude.stats import selection_sensitivity


def _scores(n=4000, seed=0):
    rng = np.random.default_rng(seed)
    y = (rng.random(n) < 0.03).astype(int)
    raw = np.clip(0.6 * y + rng.normal(0.2, 0.15, n), 0, 1)
    return y, raw


def test_elkan_threshold():
    assert elkan_threshold(CostConfig(fn=100, fp=5)) == 5 / 105


def test_brier_skill_constant_predictor_is_zero():
    y = np.array([0] * 98 + [1] * 2)
    assert abs(brier_skill(y, np.full(100, 0.02))) < 1e-12


def test_stratified_bootstrap_keeps_class_counts():
    y = np.array([0] * 90 + [1] * 10)
    vals = stratified_bootstrap(y, lambda idx: {"pos": y[idx].sum()}, n_boot=50)
    assert (vals["pos"] == 10).all()


def test_final_model_robustness_counts_and_intervals():
    y, raw = _scores()
    types = np.where(np.arange(len(y)) % 2 == 0, "TRANSFER", "CASH_OUT")
    r = final_model_robustness(y, raw, raw, threshold=0.5, types=types, n_boot=100)
    c = r["confusion"]
    assert c["tp"] + c["fp"] + c["tn"] + c["fn"] == len(y)
    lo, hi = r["ci95"]["recall"]
    assert 0 <= lo <= c["tp"] / y.sum() <= hi <= 1
    assert {t["type"] for t in r["by_type"]} == {"TRANSFER", "CASH_OUT"}
    assert {s["scenario"] for s in r["cost_sensitivity"]} >= {"moderado", "fn_20"}


def test_duplicate_effect_detects_memorized_copies():
    rng = np.random.default_rng(1)
    X = pd.DataFrame(rng.normal(size=(600, 3)), columns=["a", "b", "c"])
    y = pd.Series((rng.random(600) < 0.1).astype(int))
    X = pd.concat([X, X.iloc[:20]], ignore_index=True)
    y = pd.concat([y, y.iloc[:20]], ignore_index=True)
    train, test = np.arange(0, 400), np.arange(400, 620)
    r = duplicate_effect_fixed_model(X, y, train, test, LogisticRegression())
    assert r["frauds_with_copy"] + r["legit_with_copy"] == 20
    assert r["test_frauds"] == int(y.iloc[test].sum())


def test_selection_sensitivity_grid():
    comp = pd.DataFrame({"auc_pr_mean": [0.857, 0.856, 0.824], "equivalent_to_best": [True, True, True]},
                        index=["ens", "xgb", "mlp"])
    lat = {"ens": 2.9, "xgb": 2.05, "mlp": 1.54}
    s = selection_sensitivity(comp, lat, margins=(0.01, 0.05), tolerances=(0.5,))
    assert s.set_index("margin")["choice"].to_dict() == {0.01: "xgb", 0.05: "mlp"}

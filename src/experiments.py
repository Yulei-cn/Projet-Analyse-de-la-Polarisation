from __future__ import annotations

import csv
import statistics
from pathlib import Path

from src.generation import generate_approval_profile, generate_ranking_profile
from src.measures import phi_dH, phi_dS
from src.phi2 import phi2_approval, phi2_ranking


def _summarize(values: list[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    mean = statistics.fmean(values)
    stdev = statistics.stdev(values) if len(values) > 1 else 0.0
    return mean, stdev


def save_results_csv(rows: list[dict], output_path: str | Path) -> None:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def sweep_alpha_for_phi2_approval(
    n: int,
    m: int,
    noise: float,
    alphas: list[float],
    num_trials: int,
) -> list[dict]:
    rows = []
    for alpha in alphas:
        values = [
            phi2_approval(generate_approval_profile(n=n, m=m, alpha=alpha, noise=noise, seed=trial))
            for trial in range(num_trials)
        ]
        mean, stdev = _summarize(values)
        rows.append({"alpha": alpha, "mean": mean, "stdev": stdev})
    return rows


def sweep_alpha_for_phi2_ranking(
    n: int,
    m: int,
    noise: int,
    alphas: list[float],
    num_trials: int,
) -> list[dict]:
    rows = []
    for alpha in alphas:
        values = [
            phi2_ranking(generate_ranking_profile(n=n, m=m, alpha=alpha, noise=noise, seed=trial))
            for trial in range(num_trials)
        ]
        mean, stdev = _summarize(values)
        rows.append({"alpha": alpha, "mean": mean, "stdev": stdev})
    return rows


def sweep_alpha_for_distance_measures(
    n: int,
    m: int,
    approval_noise: float,
    ranking_noise: int,
    alphas: list[float],
    num_trials: int,
    n_init: int = 10,
) -> tuple[list[dict], list[dict]]:
    approval_rows = []
    ranking_rows = []

    for alpha in alphas:
        approval_values = [
            phi_dH(
                generate_approval_profile(n=n, m=m, alpha=alpha, noise=approval_noise, seed=trial),
                n_init=n_init,
                seed=trial,
            )
            for trial in range(num_trials)
        ]
        ranking_values = [
            phi_dS(
                generate_ranking_profile(n=n, m=m, alpha=alpha, noise=ranking_noise, seed=trial),
                n_init=n_init,
                seed=trial,
            )
            for trial in range(num_trials)
        ]

        approval_mean, approval_stdev = _summarize(approval_values)
        ranking_mean, ranking_stdev = _summarize(ranking_values)
        approval_rows.append({"alpha": alpha, "mean": approval_mean, "stdev": approval_stdev})
        ranking_rows.append({"alpha": alpha, "mean": ranking_mean, "stdev": ranking_stdev})

    return approval_rows, ranking_rows

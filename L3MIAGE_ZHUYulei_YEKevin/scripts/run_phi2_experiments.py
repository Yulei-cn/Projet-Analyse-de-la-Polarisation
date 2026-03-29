from __future__ import annotations

from src.experiments import (
    save_results_csv,
    sweep_alpha_for_phi2_approval,
    sweep_alpha_for_phi2_ranking,
)
from src.plots import plot_curve


def main() -> None:
    """Generate CSV files and figures for the phi_2 experiments."""
    alphas = [i / 10 for i in range(11)]

    approval_results = sweep_alpha_for_phi2_approval(
        n=40,
        m=6,
        noise=0.10,
        alphas=alphas,
        num_trials=20,
    )
    ranking_results = sweep_alpha_for_phi2_ranking(
        n=40,
        m=6,
        noise=1,
        alphas=alphas,
        num_trials=20,
    )

    save_results_csv(approval_results, "outputs/data/phi2_approval.csv")
    save_results_csv(ranking_results, "outputs/data/phi2_ranking.csv")
    plot_curve(approval_results, "Approval phi_2", "phi_2", "outputs/figures/phi2_approval.png")
    plot_curve(ranking_results, "Ranking phi_2", "phi_2", "outputs/figures/phi2_ranking.png")


if __name__ == "__main__":
    main()

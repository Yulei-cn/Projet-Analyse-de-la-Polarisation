from __future__ import annotations

from src.experiments import save_results_csv, sweep_alpha_for_distance_measures
from src.plots import plot_curve


def main() -> None:
    """Generate CSV files and figures for the distance-based experiments."""
    alphas = [i / 10 for i in range(11)]
    approval_results, ranking_results = sweep_alpha_for_distance_measures(
        n=40,
        m=6,
        approval_noise=0.10,
        ranking_noise=1,
        alphas=alphas,
        num_trials=10,
        n_init=10,
    )

    save_results_csv(approval_results, "outputs/data/phidh_approval.csv")
    save_results_csv(ranking_results, "outputs/data/phids_ranking.csv")
    plot_curve(approval_results, "Approval phi_dH", "phi_dH", "outputs/figures/phidh_approval.png")
    plot_curve(ranking_results, "Ranking phi_dS", "phi_dS", "outputs/figures/phids_ranking.png")


if __name__ == "__main__":
    main()

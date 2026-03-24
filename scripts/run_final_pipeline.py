from __future__ import annotations

from pathlib import Path

from src.experiments import (
    save_results_csv,
    sweep_alpha_for_distance_measures,
    sweep_alpha_for_phi2_approval,
    sweep_alpha_for_phi2_ranking,
)
from src.plots import plot_curve


def _write_summary(
    phi2_approval: list[dict],
    phi2_ranking: list[dict],
    phidh_approval: list[dict],
    phids_ranking: list[dict],
    output_path: str | Path,
) -> None:
    """Write a short markdown summary of the final experiment outputs."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    def describe(rows: list[dict], name: str) -> str:
        start = rows[0]["mean"]
        end = rows[-1]["mean"]
        return f"- `{name}`: mean rises from {start:.3f} at alpha=0.0 to {end:.3f} at alpha=1.0."

    lines = [
        "# Final Experiment Summary",
        "",
        "This file was generated automatically by `python -m scripts.run_final_pipeline`.",
        "",
        "## Configuration",
        "",
        "- `n = 40` voters",
        "- `m = 6` candidates",
        "- `alpha = 0.0, 0.1, ..., 1.0`",
        "- `phi_2` trials: `20`",
        "- distance-measure trials: `10`",
        "- k-means restarts for distance measures: `10`",
        "",
        "## Trend Summary",
        "",
        describe(phi2_approval, "phi_2 approval"),
        describe(phi2_ranking, "phi_2 ranking"),
        describe(phidh_approval, "phi_dH approval"),
        describe(phids_ranking, "phi_dS ranking"),
        "",
        "## Output Files",
        "",
        "- `outputs/data/final_phi2_approval.csv`",
        "- `outputs/data/final_phi2_ranking.csv`",
        "- `outputs/data/final_phidh_approval.csv`",
        "- `outputs/data/final_phids_ranking.csv`",
        "- `outputs/figures/final_phi2_approval.png`",
        "- `outputs/figures/final_phi2_ranking.png`",
        "- `outputs/figures/final_phidh_approval.png`",
        "- `outputs/figures/final_phids_ranking.png`",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """Run the consolidated experiment pipeline used for the final project write-up."""
    alphas = [i / 10 for i in range(11)]

    phi2_approval = sweep_alpha_for_phi2_approval(
        n=40,
        m=6,
        noise=0.10,
        alphas=alphas,
        num_trials=20,
    )
    phi2_ranking = sweep_alpha_for_phi2_ranking(
        n=40,
        m=6,
        noise=1,
        alphas=alphas,
        num_trials=20,
    )
    phidh_approval, phids_ranking = sweep_alpha_for_distance_measures(
        n=40,
        m=6,
        approval_noise=0.10,
        ranking_noise=1,
        alphas=alphas,
        num_trials=10,
        n_init=10,
    )

    save_results_csv(phi2_approval, "outputs/data/final_phi2_approval.csv")
    save_results_csv(phi2_ranking, "outputs/data/final_phi2_ranking.csv")
    save_results_csv(phidh_approval, "outputs/data/final_phidh_approval.csv")
    save_results_csv(phids_ranking, "outputs/data/final_phids_ranking.csv")

    plot_curve(phi2_approval, "Approval phi_2", "phi_2", "outputs/figures/final_phi2_approval.png")
    plot_curve(phi2_ranking, "Ranking phi_2", "phi_2", "outputs/figures/final_phi2_ranking.png")
    plot_curve(phidh_approval, "Approval phi_dH", "phi_dH", "outputs/figures/final_phidh_approval.png")
    plot_curve(phids_ranking, "Ranking phi_dS", "phi_dS", "outputs/figures/final_phids_ranking.png")

    _write_summary(
        phi2_approval,
        phi2_ranking,
        phidh_approval,
        phids_ranking,
        "outputs/final_summary.md",
    )


if __name__ == "__main__":
    main()

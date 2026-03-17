from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def plot_curve(results: list[dict], title: str, ylabel: str, output_path: str | Path) -> None:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    alphas = [row["alpha"] for row in results]
    means = [row["mean"] for row in results]
    stdevs = [row["stdev"] for row in results]

    plt.figure(figsize=(8, 5))
    plt.errorbar(alphas, means, yerr=stdevs, marker="o", capsize=4)
    plt.title(title)
    plt.xlabel("Polarization level alpha")
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output, dpi=200)
    plt.close()

from __future__ import annotations

from src.generation import generate_approval_profile, generate_ranking_profile
from src.measures import phi_dH, phi_dS
from src.phi2 import phi2_approval, phi2_ranking


def main() -> None:
    """
    Small end-to-end demo of the current codebase.

    Useful during a defense:
    - shows how generation connects to measures,
    - shows the project has one executable entry point,
    - provides quick sanity-check outputs.
    """
    approval_profile = generate_approval_profile(n=10, m=4, alpha=0.7, noise=0.1, seed=0)
    ranking_profile = generate_ranking_profile(n=10, m=4, alpha=0.7, noise=1, seed=0)

    print("Approval phi_2:", round(phi2_approval(approval_profile), 4))
    print("Ranking phi_2:", round(phi2_ranking(ranking_profile), 4))
    print("Approval phi_dH:", round(phi_dH(approval_profile, n_init=5, seed=0), 4))
    print("Ranking phi_dS:", round(phi_dS(ranking_profile, n_init=5, seed=0), 4))


if __name__ == "__main__":
    main()

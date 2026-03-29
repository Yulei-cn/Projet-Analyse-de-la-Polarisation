from __future__ import annotations

from src.clustering import kmeans2_approval, kmeans2_ranking
from src.consensus import u1_approval, u1_ranking
from src.types import ApprovalProfile, RankingProfile


def phi_dH(profile: ApprovalProfile, n_init: int = 20, seed: int | None = None) -> float:
    """
    Compute the distance-based polarization measure phi_dH for approval votes.

    Link with the project:
    - Main target for question 14 in the approval case.
    - Uses `u1_approval` and `kmeans2_approval`.
    - Studied experimentally in question 15.
    """
    if not profile:
        return 0.0
    n = len(profile)
    m = len(profile[0])
    u1 = u1_approval(profile)
    u2_tilde = kmeans2_approval(profile, n_init=n_init, seed=seed)["cost"]
    return (2 / (n * m)) * (u1 - u2_tilde)


def phi_dS(profile: RankingProfile, n_init: int = 20, seed: int | None = None) -> float:
    """
    Compute the distance-based polarization measure phi_dS for ranking votes.

    Link with the project:
    - Main target for question 14 in the ranking case.
    - Uses `u1_ranking` and `kmeans2_ranking`.
    - Studied experimentally in question 15.
    """
    if not profile:
        return 0.0
    n = len(profile)
    m = len(profile[0])
    u1 = u1_ranking(profile)
    u2_tilde = kmeans2_ranking(profile, n_init=n_init, seed=seed)["cost"]
    return (4 / (n * (m**2))) * (u1 - u2_tilde)

from __future__ import annotations

from src.clustering import kmeans2_approval, kmeans2_ranking
from src.consensus import u1_approval, u1_ranking
from src.types import ApprovalProfile, RankingProfile


def phi_dH(profile: ApprovalProfile, n_init: int = 20, seed: int | None = None) -> float:
    if not profile:
        return 0.0
    n = len(profile)
    m = len(profile[0])
    u1 = u1_approval(profile)
    u2_tilde = kmeans2_approval(profile, n_init=n_init, seed=seed)["cost"]
    return (2 / (n * m)) * (u1 - u2_tilde)


def phi_dS(profile: RankingProfile, n_init: int = 20, seed: int | None = None) -> float:
    if not profile:
        return 0.0
    n = len(profile)
    m = len(profile[0])
    u1 = u1_ranking(profile)
    u2_tilde = kmeans2_ranking(profile, n_init=n_init, seed=seed)["cost"]
    return (4 / (n * (m**2))) * (u1 - u2_tilde)

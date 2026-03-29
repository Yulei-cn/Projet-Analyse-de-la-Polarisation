from __future__ import annotations

from src.pairwise import pairwise_disagreement_approval, pairwise_disagreement_ranking
from src.types import ApprovalProfile, RankingProfile


def _phi2_from_disagreements(disagreements: dict[tuple[int, int], int], n: int, m: int) -> float:
    """
    Aggregate the pairwise values using the PDF formula for phi_2.

    For each candidate pair, the contribution is:
    (n - d^{c_k,c_l}(p)) / (n * binom(m, 2))
    """
    if n == 0 or m < 2:
        return 0.0
    pair_count = m * (m - 1) / 2
    scale = n * pair_count
    return sum((n - value) / scale for value in disagreements.values())


def phi2_approval(profile: ApprovalProfile) -> float:
    """
    Compute the first version of phi_2 for approval profiles.

    Link with the project:
    - Target function for question 5 in the approval case.
    - Used in question 6 experiments through `sweep_alpha_for_phi2_approval`.
    - Depends on `pairwise_disagreement_approval`.
    """
    if not profile:
        return 0.0
    return _phi2_from_disagreements(pairwise_disagreement_approval(profile), len(profile), len(profile[0]))


def phi2_ranking(profile: RankingProfile) -> float:
    """
    Compute the first version of phi_2 for ranking profiles.

    Link with the project:
    - Target function for question 5 in the ranking case.
    - Used in question 6 experiments through `sweep_alpha_for_phi2_ranking`.
    - Depends on `pairwise_disagreement_ranking`.
    """
    if not profile:
        return 0.0
    return _phi2_from_disagreements(pairwise_disagreement_ranking(profile), len(profile), len(profile[0]))

from __future__ import annotations

from src.pairwise import pairwise_disagreement_approval, pairwise_disagreement_ranking
from src.types import ApprovalProfile, RankingProfile


def _phi2_from_disagreements(disagreements: dict[tuple[int, int], int], n: int, m: int) -> float:
    if n == 0 or m < 2:
        return 0.0
    scale = n * (m * (m - 1) / 2)
    return sum((2 * value) / scale for value in disagreements.values())


def phi2_approval(profile: ApprovalProfile) -> float:
    if not profile:
        return 0.0
    return _phi2_from_disagreements(pairwise_disagreement_approval(profile), len(profile), len(profile[0]))


def phi2_ranking(profile: RankingProfile) -> float:
    if not profile:
        return 0.0
    return _phi2_from_disagreements(pairwise_disagreement_ranking(profile), len(profile), len(profile[0]))

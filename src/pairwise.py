from __future__ import annotations

from itertools import combinations

from src.types import ApprovalProfile, RankingProfile


def pairwise_disagreement_approval(profile: ApprovalProfile) -> dict[tuple[int, int], int]:
    if not profile:
        return {}

    m = len(profile[0])
    result: dict[tuple[int, int], int] = {}
    for i, j in combinations(range(m), 2):
        left = 0
        right = 0
        for ballot in profile:
            if ballot[i] > ballot[j]:
                left += 1
            elif ballot[j] > ballot[i]:
                right += 1
        result[(i, j)] = min(left, right)
    return result


def pairwise_disagreement_ranking(profile: RankingProfile) -> dict[tuple[int, int], int]:
    if not profile:
        return {}

    m = len(profile[0])
    result: dict[tuple[int, int], int] = {}
    for i, j in combinations(range(m), 2):
        left = 0
        right = 0
        for order in profile:
            if order.index(i) < order.index(j):
                left += 1
            else:
                right += 1
        result[(i, j)] = min(left, right)
    return result

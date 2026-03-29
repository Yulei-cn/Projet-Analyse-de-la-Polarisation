from __future__ import annotations

from itertools import combinations

from src.types import ApprovalProfile, RankingProfile


def pairwise_disagreement_approval(profile: ApprovalProfile) -> dict[tuple[int, int], int]:
    """
    Compute d^{c_k,c_l}(p) for each pair of candidates in approval.

    Link with the project:
    - This is the building block for question 3 in the approval setting.
    - Its output is aggregated by `phi2_approval`.
    - For approval votes, n_{k,l}(p) counts voters such that a[k] = 1 and
      a[l] = 0, and this function returns |n_{k,l}(p) - n_{l,k}(p)|.
    """
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
        result[(i, j)] = abs(left - right)
    return result


def pairwise_disagreement_ranking(profile: RankingProfile) -> dict[tuple[int, int], int]:
    """
    Compute d^{c_k,c_l}(p) for each pair of candidates in rankings.

    Link with the project:
    - This is the building block for question 3 in the ranking setting.
    - Its output is aggregated by `phi2_ranking`.
    - For ranking votes, n_{k,l}(p) counts voters ranking c_k ahead of c_l,
      and this function returns |n_{k,l}(p) - n_{l,k}(p)|.
    """
    if not profile:
        return {}

    m = len(profile[0])
    result: dict[tuple[int, int], int] = {}
    position_maps = [{candidate: rank for rank, candidate in enumerate(order)} for order in profile]
    for i, j in combinations(range(m), 2):
        left = 0
        right = 0
        for positions in position_maps:
            if positions[i] < positions[j]:
                left += 1
            else:
                right += 1
        result[(i, j)] = abs(left - right)
    return result

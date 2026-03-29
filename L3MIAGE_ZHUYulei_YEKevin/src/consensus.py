from __future__ import annotations

from collections import Counter
from functools import lru_cache

from src.distances import hamming_distance, spearman_distance
from src.types import ApprovalBallot, ApprovalProfile, RankingBallot, RankingProfile


def approval_consensus_ballot(profile: ApprovalProfile) -> ApprovalBallot:
    """
    Build the approval consensus ballot by majority vote on each coordinate.

    Link with the project:
    - This is the constructive part behind question 10.
    - Reused by `u1_approval` and by the centroid update in `kmeans2_approval`.
    """
    if not profile:
        return []
    n = len(profile)
    m = len(profile[0])
    consensus: ApprovalBallot = []
    for j in range(m):
        ones = sum(ballot[j] for ballot in profile)
        consensus.append(1 if ones * 2 >= n else 0)
    return consensus


def u1_approval(profile: ApprovalProfile) -> int:
    """
    Compute the global consensus cost u1 for an approval profile.

    Link with the project:
    - Main value studied in questions 10 and 12 for approval votes.
    - Reused later by `phi_dH`.
    """
    consensus = approval_consensus_ballot(profile)
    return sum(hamming_distance(consensus, ballot) for ballot in profile)


def ranking_assignment_costs(profile: RankingProfile) -> list[list[int]]:
    """
    Build the candidate-position cost matrix for the ranking consensus problem.

    Link with the project:
    - This matches the assignment view suggested in question 11.
    - Entry (candidate, position) is the total Spearman contribution obtained by
      placing that candidate at that position in the consensus ranking.
    """
    if not profile:
        return []

    m = len(profile[0])
    position_maps = [[0] * m for _ in profile]
    for voter_index, order in enumerate(profile):
        for rank, candidate in enumerate(order):
            position_maps[voter_index][candidate] = rank

    costs = [[0] * m for _ in range(m)]
    for candidate in range(m):
        for position in range(m):
            costs[candidate][position] = sum(
                abs(position_maps[voter_index][candidate] - position)
                for voter_index in range(len(profile))
            )
    return costs


def ranking_consensus_ballot(profile: RankingProfile) -> RankingBallot:
    """
    Build an optimal consensus ranking for Spearman distance.

    Link with the project:
    - This is the constructive part behind questions 11 and 12.
    - Reused by `u1_ranking` and by the centroid update in `kmeans2_ranking`.
    - The implementation solves the candidate-position assignment problem exactly
      with dynamic programming on subsets.
    """
    if not profile:
        return []

    costs = ranking_assignment_costs(profile)
    m = len(costs)

    @lru_cache(maxsize=None)
    def best_cost(position: int, used_mask: int) -> int:
        if position == m:
            return 0

        best = float("inf")
        for candidate in range(m):
            if used_mask & (1 << candidate):
                continue
            candidate_cost = costs[candidate][position] + best_cost(position + 1, used_mask | (1 << candidate))
            if candidate_cost < best:
                best = candidate_cost
        return int(best)

    consensus: RankingBallot = []
    used_mask = 0
    for position in range(m):
        best_candidate = -1
        best_candidate_cost = float("inf")
        for candidate in range(m):
            if used_mask & (1 << candidate):
                continue
            candidate_cost = costs[candidate][position] + best_cost(position + 1, used_mask | (1 << candidate))
            if candidate_cost < best_candidate_cost:
                best_candidate = candidate
                best_candidate_cost = candidate_cost
        consensus.append(best_candidate)
        used_mask |= 1 << best_candidate

    return consensus


def u1_ranking(profile: RankingProfile) -> int:
    """
    Compute the global consensus cost u1 for a ranking profile.

    Link with the project:
    - Main value studied in questions 11 and 12 for ranking votes.
    - Reused later by `phi_dS`.
    """
    consensus = ranking_consensus_ballot(profile)
    return sum(spearman_distance(consensus, ballot) for ballot in profile)


def most_common_ballot(profile: RankingProfile) -> RankingBallot:
    """Return the most frequent ranking ballot in a profile."""
    counter = Counter(tuple(ballot) for ballot in profile)
    if not counter:
        return []
    return list(counter.most_common(1)[0][0])

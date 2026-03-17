from __future__ import annotations

from collections import Counter

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


def ranking_consensus_ballot(profile: RankingProfile) -> RankingBallot:
    """
    Build a first ranking consensus ballot using average candidate positions.

    Link with the project:
    - This is a provisional implementation for questions 11 and 12.
    - Reused by `u1_ranking` and by the centroid update in `kmeans2_ranking`.

    Note:
    - For the final version, this may need to be replaced by a method aligned
      exactly with the matching-based formulation mentioned in the PDF.
    """
    if not profile:
        return []
    m = len(profile[0])
    average_rank = [0.0] * m
    for order in profile:
        for rank, candidate in enumerate(order):
            average_rank[candidate] += rank
    n = len(profile)
    for candidate in range(m):
        average_rank[candidate] /= n
    return sorted(range(m), key=lambda candidate: (average_rank[candidate], candidate))


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

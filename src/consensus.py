from __future__ import annotations

from collections import Counter

from src.distances import hamming_distance, spearman_distance
from src.types import ApprovalBallot, ApprovalProfile, RankingBallot, RankingProfile


def approval_consensus_ballot(profile: ApprovalProfile) -> ApprovalBallot:
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
    consensus = approval_consensus_ballot(profile)
    return sum(hamming_distance(consensus, ballot) for ballot in profile)


def ranking_consensus_ballot(profile: RankingProfile) -> RankingBallot:
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
    consensus = ranking_consensus_ballot(profile)
    return sum(spearman_distance(consensus, ballot) for ballot in profile)


def most_common_ballot(profile: RankingProfile) -> RankingBallot:
    counter = Counter(tuple(ballot) for ballot in profile)
    if not counter:
        return []
    return list(counter.most_common(1)[0][0])

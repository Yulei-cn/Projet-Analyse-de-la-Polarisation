from __future__ import annotations

from src.types import ApprovalBallot, RankingBallot


def hamming_distance(a: ApprovalBallot, b: ApprovalBallot) -> int:
    if len(a) != len(b):
        raise ValueError("approval ballots must have the same length")
    return sum(left != right for left, right in zip(a, b))


def ranking_to_positions(order: RankingBallot) -> list[int]:
    positions = [0] * len(order)
    for rank, candidate in enumerate(order):
        positions[candidate] = rank
    return positions


def spearman_distance(order1: RankingBallot, order2: RankingBallot) -> int:
    if len(order1) != len(order2):
        raise ValueError("ranking ballots must have the same length")
    pos1 = ranking_to_positions(order1)
    pos2 = ranking_to_positions(order2)
    return sum(abs(a - b) for a, b in zip(pos1, pos2))

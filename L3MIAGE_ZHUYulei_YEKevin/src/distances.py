from __future__ import annotations

from src.types import ApprovalBallot, RankingBallot


def hamming_distance(a: ApprovalBallot, b: ApprovalBallot) -> int:
    """
    Compute the Hamming distance between two approval ballots.

    Link with the project:
    - Implements the distance used in questions 7 and 8 for approval votes.
    - Reused by `u1_approval`, `kmeans2_approval` and `phi_dH`.
    """
    if len(a) != len(b):
        raise ValueError("approval ballots must have the same length")
    return sum(left != right for left, right in zip(a, b))


def ranking_to_positions(order: RankingBallot) -> list[int]:
    """
    Convert an order representation into a rank-position table.

    Example:
    if `order = [2, 0, 1]`, candidate 2 is rank 0, candidate 0 is rank 1,
    candidate 1 is rank 2.

    Link with the project:
    - Utility used by `spearman_distance`.
    """
    positions = [0] * len(order)
    for rank, candidate in enumerate(order):
        positions[candidate] = rank
    return positions


def spearman_distance(order1: RankingBallot, order2: RankingBallot) -> int:
    """
    Compute the Spearman distance between two total orders.

    Link with the project:
    - Implements the distance used in questions 7 and 8 for ranking votes.
    - Reused by `u1_ranking`, `kmeans2_ranking` and `phi_dS`.
    """
    if len(order1) != len(order2):
        raise ValueError("ranking ballots must have the same length")
    pos1 = ranking_to_positions(order1)
    pos2 = ranking_to_positions(order2)
    return sum(abs(a - b) for a, b in zip(pos1, pos2))

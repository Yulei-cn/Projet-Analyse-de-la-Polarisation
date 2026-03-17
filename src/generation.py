from __future__ import annotations

import random

from src.types import ApprovalBallot, ApprovalProfile, RankingBallot, RankingProfile


def _flip_with_probability(ballot: ApprovalBallot, noise: float, rng: random.Random) -> ApprovalBallot:
    return [bit if rng.random() >= noise else 1 - bit for bit in ballot]


def _random_swaps(order: RankingBallot, swaps: int, rng: random.Random) -> RankingBallot:
    result = order[:]
    size = len(result)
    for _ in range(max(0, swaps)):
        i, j = rng.sample(range(size), 2)
        result[i], result[j] = result[j], result[i]
    return result


def generate_approval_profile(
    n: int,
    m: int,
    alpha: float,
    noise: float,
    seed: int | None = None,
) -> ApprovalProfile:
    if n <= 0 or m <= 0:
        raise ValueError("n and m must be positive")
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must be in [0, 1]")
    if not 0.0 <= noise <= 1.0:
        raise ValueError("noise must be in [0, 1]")

    rng = random.Random(seed)
    center = [rng.randint(0, 1) for _ in range(m)]
    opposite = [1 - bit for bit in center]

    polarized_count = round(alpha * n / 2) * 2
    first_block = (n - polarized_count) + polarized_count // 2
    second_block = n - first_block

    profile: ApprovalProfile = []
    for _ in range(first_block):
        profile.append(_flip_with_probability(center, noise, rng))
    for _ in range(second_block):
        profile.append(_flip_with_probability(opposite, noise, rng))

    rng.shuffle(profile)
    return profile


def generate_ranking_profile(
    n: int,
    m: int,
    alpha: float,
    noise: int,
    seed: int | None = None,
) -> RankingProfile:
    if n <= 0 or m <= 0:
        raise ValueError("n and m must be positive")
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must be in [0, 1]")
    if noise < 0:
        raise ValueError("noise must be non-negative")

    rng = random.Random(seed)
    center = list(range(m))
    rng.shuffle(center)
    opposite = list(reversed(center))

    polarized_count = round(alpha * n / 2) * 2
    first_block = (n - polarized_count) + polarized_count // 2
    second_block = n - first_block

    profile: RankingProfile = []
    for _ in range(first_block):
        profile.append(_random_swaps(center, noise, rng))
    for _ in range(second_block):
        profile.append(_random_swaps(opposite, noise, rng))

    rng.shuffle(profile)
    return profile

from __future__ import annotations

import random

from src.consensus import approval_consensus_ballot, ranking_consensus_ballot
from src.distances import hamming_distance, spearman_distance
from src.types import ApprovalProfile, RankingProfile


def _assignment_changed(old_labels: list[int] | None, new_labels: list[int]) -> bool:
    return old_labels is None or old_labels != new_labels


def kmeans2_approval(
    profile: ApprovalProfile,
    n_init: int = 20,
    seed: int | None = None,
    max_iter: int = 100,
) -> dict:
    if len(profile) < 2:
        return {"cost": 0, "centroids": profile[:], "labels": [0] * len(profile)}

    rng = random.Random(seed)
    best: dict | None = None

    for _ in range(n_init):
        centroids = [ballot[:] for ballot in rng.sample(profile, 2)]
        labels: list[int] | None = None

        for _ in range(max_iter):
            new_labels = []
            for ballot in profile:
                d0 = hamming_distance(ballot, centroids[0])
                d1 = hamming_distance(ballot, centroids[1])
                new_labels.append(0 if d0 <= d1 else 1)

            if not _assignment_changed(labels, new_labels):
                break
            labels = new_labels

            clusters = [[ballot for ballot, label in zip(profile, labels) if label == idx] for idx in range(2)]
            for idx in range(2):
                if clusters[idx]:
                    centroids[idx] = approval_consensus_ballot(clusters[idx])

        final_labels = labels or [0] * len(profile)
        cost = sum(
            hamming_distance(ballot, centroids[label])
            for ballot, label in zip(profile, final_labels)
        )
        candidate = {"cost": cost, "centroids": centroids, "labels": final_labels}
        if best is None or candidate["cost"] < best["cost"]:
            best = candidate

    return best or {"cost": 0, "centroids": [], "labels": []}


def kmeans2_ranking(
    profile: RankingProfile,
    n_init: int = 20,
    seed: int | None = None,
    max_iter: int = 100,
) -> dict:
    if len(profile) < 2:
        return {"cost": 0, "centroids": profile[:], "labels": [0] * len(profile)}

    rng = random.Random(seed)
    best: dict | None = None

    for _ in range(n_init):
        centroids = [ballot[:] for ballot in rng.sample(profile, 2)]
        labels: list[int] | None = None

        for _ in range(max_iter):
            new_labels = []
            for ballot in profile:
                d0 = spearman_distance(ballot, centroids[0])
                d1 = spearman_distance(ballot, centroids[1])
                new_labels.append(0 if d0 <= d1 else 1)

            if not _assignment_changed(labels, new_labels):
                break
            labels = new_labels

            clusters = [[ballot for ballot, label in zip(profile, labels) if label == idx] for idx in range(2)]
            for idx in range(2):
                if clusters[idx]:
                    centroids[idx] = ranking_consensus_ballot(clusters[idx])

        final_labels = labels or [0] * len(profile)
        cost = sum(
            spearman_distance(ballot, centroids[label])
            for ballot, label in zip(profile, final_labels)
        )
        candidate = {"cost": cost, "centroids": centroids, "labels": final_labels}
        if best is None or candidate["cost"] < best["cost"]:
            best = candidate

    return best or {"cost": 0, "centroids": [], "labels": []}

from src.clustering import kmeans2_approval, kmeans2_ranking
from src.consensus import ranking_consensus_ballot, u1_approval, u1_ranking


def test_u2_is_not_greater_than_u1_for_approval() -> None:
    profile = [[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0]]
    assert kmeans2_approval(profile, n_init=5, seed=0)["cost"] <= u1_approval(profile)


def test_ranking_consensus_ballot_matches_obvious_profile() -> None:
    profile = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    assert ranking_consensus_ballot(profile) == [0, 1, 2]


def test_u1_ranking_is_zero_on_identical_profile() -> None:
    profile = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    assert u1_ranking(profile) == 0


def test_u2_is_not_greater_than_u1_for_ranking() -> None:
    profile = [[0, 1, 2], [0, 1, 2], [2, 1, 0], [2, 1, 0]]
    assert kmeans2_ranking(profile, n_init=5, seed=0)["cost"] <= u1_ranking(profile)

from src.clustering import kmeans2_approval
from src.consensus import u1_approval


def test_u2_is_not_greater_than_u1_for_approval() -> None:
    profile = [[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0]]
    assert kmeans2_approval(profile, n_init=5, seed=0)["cost"] <= u1_approval(profile)

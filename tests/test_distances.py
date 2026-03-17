from src.distances import hamming_distance, spearman_distance


def test_hamming_distance_basic() -> None:
    assert hamming_distance([1, 0, 1], [1, 1, 0]) == 2


def test_spearman_distance_zero_on_equal_ballots() -> None:
    order = [0, 1, 2, 3]
    assert spearman_distance(order, order) == 0

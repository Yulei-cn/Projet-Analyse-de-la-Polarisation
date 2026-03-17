from src.phi2 import phi2_approval, phi2_ranking


def test_phi2_approval_zero_on_identical_profile() -> None:
    profile = [[1, 0], [1, 0], [1, 0], [1, 0]]
    assert phi2_approval(profile) == 0.0


def test_phi2_ranking_zero_on_identical_profile() -> None:
    profile = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    assert phi2_ranking(profile) == 0.0


def test_phi2_approval_is_one_for_perfect_two_pole_case_with_two_candidates() -> None:
    profile = [[1, 0], [1, 0], [0, 1], [0, 1]]
    assert phi2_approval(profile) == 1.0


def test_phi2_ranking_is_one_for_perfect_two_pole_case_with_two_candidates() -> None:
    profile = [[0, 1], [0, 1], [1, 0], [1, 0]]
    assert phi2_ranking(profile) == 1.0

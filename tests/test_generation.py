from src.generation import generate_approval_profile, generate_ranking_profile


def test_generate_approval_profile_shape() -> None:
    profile = generate_approval_profile(n=10, m=4, alpha=0.5, noise=0.1, seed=0)
    assert len(profile) == 10
    assert all(len(ballot) == 4 for ballot in profile)


def test_generate_ranking_profile_shape() -> None:
    profile = generate_ranking_profile(n=8, m=5, alpha=0.5, noise=1, seed=0)
    assert len(profile) == 8
    assert all(sorted(ballot) == list(range(5)) for ballot in profile)

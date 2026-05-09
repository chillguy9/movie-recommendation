from app.recommender import recommend


def test_recommend_valid_movie():
    recommendations = recommend("avatar")
    assert isinstance(recommendations, list)
    assert len(recommendations) == 5
    assert all(isinstance(title, str) for title in recommendations)


def test_recommend_invalid_movie():
    assert recommend("this movie does not exist") == ""

from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .utils import extract_cast, extract_director, extract_genres, stem_text

ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
MOVIES_CSV = RAW_DATA_DIR / "tmdb_5000_movies.csv"
CREDITS_CSV = RAW_DATA_DIR / "tmdb_5000_credits.csv"


def load_movie_data() -> pd.DataFrame:
    """Load raw datasets, merge them, and prepare the movie feature matrix."""
    movies = pd.read_csv(MOVIES_CSV)
    credits = pd.read_csv(CREDITS_CSV)

    movies = pd.merge(movies, credits, on="title")
    movies = movies[["movie_id", "title", "genres", "keywords", "overview", "cast", "crew"]].copy()
    movies = movies.dropna()

    movies["genres"] = movies["genres"].apply(extract_genres)
    movies["keywords"] = movies["keywords"].apply(extract_genres)
    movies["cast"] = movies["cast"].apply(extract_cast)
    movies["crew"] = movies["crew"].apply(extract_director)

    movies["overview"] = (
        movies["genres"]
        + " "
        + movies["keywords"]
        + " "
        + movies["overview"]
        + " "
        + movies["cast"]
        + " "
        + movies["crew"]
    )

    movies = movies[["movie_id", "title", "overview"]].copy()
    movies["overview"] = movies["overview"].apply(stem_text)
    movies["title"] = movies["title"].str.lower()

    return movies


MOVIE_DATA = load_movie_data()
VECTORIZER = CountVectorizer(max_features=5000, stop_words="english")
MOVIE_MATRIX = VECTORIZER.fit_transform(MOVIE_DATA["overview"]).toarray()
SIMILARITY_MATRIX = cosine_similarity(MOVIE_MATRIX)


def recommend(movie_title: str, limit: int = 5):
    """Return a list of similar movie titles given a movie name."""
    try:
        normalized_title = movie_title.strip().lower()
        index = MOVIE_DATA[MOVIE_DATA["title"] == normalized_title].index[0]
        similarity_scores = list(enumerate(SIMILARITY_MATRIX[index]))
        similarity_scores.sort(reverse=True, key=lambda item: item[1])

        recommended_titles = [MOVIE_DATA["title"][score[0]] for score in similarity_scores[1 : limit + 1]]
        return recommended_titles
    except Exception:
        return ""

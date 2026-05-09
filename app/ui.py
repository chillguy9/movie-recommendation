import streamlit as st

from .recommender import recommend


def _render_style() -> None:
    st.markdown(
        """
        <style>
        .recommend-card {
            background: #f8f9fa;
            border-radius: 14px;
            padding: 14px 18px;
            margin-bottom: 10px;
            box-shadow: 0 1px 6px rgba(15, 23, 42, 0.08);
        }
        .recommend-card p {
            margin: 0;
            font-size: 1rem;
            font-weight: 600;
            color: #111827;
        }
        .stButton>button {
            background-color: #2563eb;
            color: #ffffff;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #1d4ed8;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    """Render the Streamlit application interface."""
    st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="centered")

    _render_style()

    st.title("🎬 Movie Recommendation System")
    st.write(
        "Use the movie title search box below to get a list of similar films based on plot, cast, genres, and keywords."
    )

    movie_name = st.text_input("Movie name", placeholder="e.g. The Dark Knight")

    if st.button("Recommend"):
        movie_name_clean = movie_name.strip().lower()

        if not movie_name_clean:
            st.error("Please enter a movie name before requesting recommendations.")
            return

        recommendations = recommend(movie_name_clean)

        if not recommendations:
            st.error(
                "Movie not found or no recommendations are available. Try a different title from the dataset."
            )
            return

        st.success(f"Recommended movies for '{movie_name.strip()}'")

        for title in recommendations:
            st.markdown(
                f"<div class='recommend-card'><p>{title.title()}</p></div>",
                unsafe_allow_html=True,
            )

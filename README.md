# Movie Recommendation System

A professional Streamlit project that recommends movies using content-based similarity.
This repository is organized for maintainability, scalability, and portfolio showcase.

## Features

- Search for a movie title and receive five similar movie recommendations
- Content-based recommendations using plot, genres, keywords, cast, and director
- Beginner-friendly Streamlit interface with clear feedback and styling
- Modular architecture for easy maintenance and testing

## Tech Stack

- Python
- Streamlit
- pandas
- NumPy
- scikit-learn
- NLTK

## Folder Structure

```text
movie-recommendation-system/
├── app/
│   ├── __init__.py
│   ├── recommender.py
│   ├── ui.py
│   └── utils.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── models/
├── assets/
│   └── screenshots/
├── tests/
├── .github/
│   └── workflows/
├── app.py
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── LICENSE
└── setup.py
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd movie-recommendation-system
```

2. Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Launch the Streamlit app with:

```bash
streamlit run app.py
```

## Screenshots

Add UI screenshots to the `assets/screenshots/` directory and reference them here.

## Future Improvements

- Add user authentication and saved recommendation lists
- Introduce collaborative filtering or hybrid recommendation methods
- Build REST API endpoints for the recommendation engine
- Add more tests and CI coverage for data processing logic

## Contributing

Contributions are welcome! Please review `CONTRIBUTING.md` for guidelines.

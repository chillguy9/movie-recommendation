from setuptools import find_packages, setup

setup(
    name="movie-recommendation-system",
    version="0.1.0",
    description="A Streamlit-based movie recommendation application using content-based similarity.",
    author="Movie Recommendation Project",
    author_email="noreply@example.com",
    python_requires=">=3.10",
    packages=find_packages(include=["app", "app.*"]),
    install_requires=[
        "streamlit>=1.57.0",
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "nltk>=3.9.4",
        "scikit-learn>=1.8.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

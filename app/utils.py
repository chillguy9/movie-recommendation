import json
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def extract_genres(value: str) -> str:
    """Extract a space-separated list of genre names from a JSON string."""
    try:
        parsed = json.loads(value)
        names = [item.get("name", "") for item in parsed]
        return " ".join(names)
    except (TypeError, ValueError):
        return ""


def extract_cast(value: str) -> str:
    """Extract the first three cast member names from a JSON string."""
    try:
        parsed = json.loads(value)
        names = [item.get("name", "") for item in parsed]
        return " ".join(names[:3])
    except (TypeError, ValueError):
        return ""


def extract_director(value: str) -> str:
    """Return the director name from the crew JSON string."""
    try:
        parsed = json.loads(value)
        for item in parsed:
            if item.get("job") == "Director":
                return item.get("name", "")
    except (TypeError, ValueError):
        return ""
    return ""


def stem_text(text: str) -> str:
    """Stem each word in the provided text using PorterStemmer."""
    try:
        tokens = [ps.stem(word) for word in text.split()]
        return " ".join(tokens)
    except TypeError:
        return ""

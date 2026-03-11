import nltk
from nltk.corpus import wordnet #definitions, synonyms, antonyms

DICTIONARY = {
    "fr": {},
    "en": {}
}

def get_random_word(language: str, level: int) -> str:
    """Return a random word in the dictionary of the choosed language corresponding to the level.
    Input:
        - language:  language of the chosen word in ["fr", "en", "es", "de", "it", "po"]
        - level: level of the chosen word in [1,2,3]
    Output:
        - word: a word
    """
    if language not in DICTIONARY:
        raise ValueError(f"The selected language {language} is not supported.")


def word_exists(word: str, language: str) -> bool:
    """Vérifie si un mot existe dans le dictionnaire de la langue cible."""

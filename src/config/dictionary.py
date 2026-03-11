import nltk
from nltk.corpus import wordnet as wn # Select words according to their part of speech

# For french dictionary :
nltk.download('wordnet')
nltk.download('omw-1.4')

###### Dictionary definition ######

# SUPPORTED_LANGUAGES = ["en", "fr"] # add:  "es", "de", "it", "po"

# ENGLISH
nouns       = set(w.name() for s in wn.all_synsets('n') for w in s.lemmas())
verbs     = set(w.name() for s in wn.all_synsets('v') for w in s.lemmas())
adjectives  = set(w.name() for s in wn.all_synsets('a') for w in s.lemmas())
adverbs   = set(w.name() for s in wn.all_synsets('r') for w in s.lemmas())
dict_en = nouns | verbs | adjectives | adverbs

# FRANCAIS
noms      = set(w.name() for s in wn.all_synsets('n') for w in s.lemmas(lang='fra'))
verbes    = set(w.name() for s in wn.all_synsets('v') for w in s.lemmas(lang='fra'))
adjectifs = set(w.name() for s in wn.all_synsets('a') for w in s.lemmas(lang='fra'))
adverbes  = set(w.name() for s in wn.all_synsets('r') for w in s.lemmas(lang='fra'))
dict_fr = noms | verbes | adjectifs | adverbes

DICTIONARY = {
    "en": dict_en,
    "fr": dict_fr
}

def get_random_word(language: str, level: int) -> str:
    """Return a random word in the dictionary of the choosed language corresponding to the level.
    Input:
        - language:  language of the chosen word in ["fr", "en"]
        - level: level of the chosen word in [1,2,3]
    Output:
        - word: a word
    """
    if language not in DICTIONARY:
        raise ValueError(f"The selected language {language} is not supported.")



def word_exists(word: str, language: str) -> bool:
    """Vérifie si un mot existe dans le dictionnaire de la langue cible."""

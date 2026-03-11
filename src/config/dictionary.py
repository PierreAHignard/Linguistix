import pandas as pd
from pathlib import Path

import nltk
from nltk.corpus import wordnet as wn # Select words according to their part of speech

# For french dictionary :
nltk.download('wordnet')
nltk.download('omw-1.4')

###### Dictionary definition ######

def is_valid_word(mot):
    """
    Check if a word is a valid simple word.
    Excludes compound words (with '_' or spaces), proper nouns (starting
    with a capital letter), and words containing numbers.

    Inputs:
        mot: The word to validate.

    Outputs:
        bool: True if the word is valid, False otherwise.
    """
    # Exclude compound words (containing _, space, hyphen)
    if '_' in mot or ' ' in mot:
        return False
    # Exclude proper nouns (starting with a capital letter)
    if mot[0].isupper():
        return False
    # Exclude words with numbers
    if not all(c.isalpha() for c in mot):
        return False
    return True

# ENGLISH
nouns       = set(w.name() for s in wn.all_synsets('n') for w in s.lemmas())
verbs     = set(w.name() for s in wn.all_synsets('v') for w in s.lemmas())
adjectives  = set(w.name() for s in wn.all_synsets('a') for w in s.lemmas())
adverbs   = set(w.name() for s in wn.all_synsets('r') for w in s.lemmas())
dict_en = [mot for mot in (nouns | verbs | adjectives | adverbs) if is_valid_word(mot)]

# FRANCAIS
df_fr = pd.read_csv(Path(__file__).parent.parent/'data'/'french_glossary.tsv', sep='\t')
# Filtres
df_fr_filter = df_fr[
        (df_fr['cgram'] in ['NOM', "VER", "ADJ"]) &              # common nouns only
        (df_fr['nblettres'] >= 2) &
        (df_fr['islem'] == 1) &                              # not simple letters (nouns in the dataset)
        (~df_fr['ortho'].str.contains(r'[-\s_]', regex=True)) &  # excludes compound words
        (df_fr['ortho'].str.match(r'^[a-zàâäéèêëîïôöùûüÿç]+$')) # French letters only
    ][['lemme', 'cgram', 'freqlemfilms2', 'freqlemlivres', '']].drop_duplicates()

dict_fr = df_fr_filter['lemme'].tolist()

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

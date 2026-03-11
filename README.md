# Linguistix
Structure du projet :

```
src/
├── config/
│   ├── modes.py          # Constantes et définitions des modes/niveaux
│   └── dictionary.py     # Dictionnaire de mots par langue
│
├── core/
│   ├── game_state.py     # État global (mot cible, essais, mode, langue)
│   ├── preprocessing.py  # Validation entrée + comptage essais
│   └── postprocessing.py # Formatage des réponses
│
├── modes/
│   ├── memory_mode.py    # Prompts système pour mode Mémoire (niv 1 & 2)
│   ├── learning_mode.py  # Prompts système pour Apprentissage (niv 1, 2, 3)
│   └── game_mode.py      # Prompts système pour Jeu
│
├── api/
│   └── claude_client.py  # Wrapper Anthropic SDK + gestion historique
│
└── main.py               # Point d'entrée + boucle principale (CLI ou Streamlit)
```
## 1. Interface initiale
Interface Gradio

- Choix de la difficulté des mots (seulement noms, verbes, adjectifs et adverbes)
- Choix de la langue 
- Objectif utilisateur :
    * **Mémoire** : 
        Commence par donner une définition du mot (sans utiliser de mots cémantiquement proches).

        **a. Niveau 1** : 
        Répond aux questions en donnant des indices (seulement dans la langue choisie)

        **b. Niveau 2** : 
        Ne répond pas aux questions, dit seuelemtn si le mot est roche ou non

    * **Apprentissage d'une langue** :

        **a. Niveau 1** :
            L'utilisateur peut parler dans la langue qu'il veut pour les indices, et le chatbot répond dans la même langue
            Il peut poser soit des questions et le chatbot répond par un indice soit l'utilisateur donne 1 mot et le chatbot indique si le mot est proche ou pas + redonne les 5 meilleurs mots qu'a déjà donné l'utilisateur

        **b. Niveau 2** :
            Idem niveau 1 mais réponses seulement dans la langue cible.

        **c. Niveau 3** :
            Idem niveau 1 mais réponses seulement dans la langue cible et le chatbot ne répond pas si la question est dans une autre langue.

    * **Jeu** : 
        Ne répond pas aux questions, dit seuelemtn si le mot est roche ou non, par de nul part

## 2. Preprocessing
- Si les questions ne sont pas autorisées, le préprocessing renvoie un message d'erreur
- Les mots sont choisis dans un dictionnaire prédéfini
- Test que le mot de l'utilisateur existe bien dans le dictionnaire, si ce n'est pas le cas, ne pas compter l'essais
- Compte le nombre d'essais

## 3. Postprocessing
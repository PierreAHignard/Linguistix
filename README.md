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

## Dataset Presentation

### French_glossary
Voici les 35 colonnes de Lexique383, regroupées par thème :

## Identification du mot

| Colonne | Description | Exemple |
|---|---|---|
| `ortho` | Forme orthographique (le mot tel qu'écrit) | `chienne` |
| `phon` | Forme phonologique | `SjEn` |
| `lemme` | Forme canonique du mot | `chien` |
| `cgram` | Catégorie grammaticale | `NOM`, `VER`, `ADJ`... |
| `genre` | Genre | `m`, `f` |
| `nombre` | Nombre | `s`, `p` |
| `islem` | Vrai si la forme est elle-même un lemme | `True`/`False` |
| `infover` | Pour les verbes : mode, temps, personne | `ind:pre:3s` |

## Fréquences

| Colonne | Description |
|---|---|
| `freqlemfilms2` | Fréquence du **lemme** dans les sous-titres de films (par million) |
| `freqlemlivres` | Fréquence du **lemme** dans les livres (par million) |
| `freqfilms2` | Fréquence de la **forme** dans les sous-titres de films |
| `freqlivres` | Fréquence de la **forme** dans les livres |

## Structure orthographique et phonologique

| Colonne | Description | Exemple |
|---|---|---|
| `nblettres` | Nombre de lettres | `7` |
| `nbphons` | Nombre de phonèmes | `4` |
| `cvcv` | Structure orthographique (C=consonne, V=voyelle) | `CCVVCCV` |
| `p_cvcv` | Structure phonologique | `CYVC` |
| `syll` | Forme phonologique syllabée | `m@-Ze` |
| `nbsyll` | Nombre de syllabes | `2` |
| `cv_cv` | Structure phonologique syllabée | `CV-CV` |
| `orthosyll` | Syllabation orthographique | `man-ger` |
| `orthrenv` | Mot orthographique à l'envers | `regnam` |
| `phonrenv` | Forme phonologique à l'envers | `eZ@m` |

## Voisins lexicaux

| Colonne | Description |
|---|---|
| `voisorth` | Nombre de voisins orthographiques (mots à 1 lettre près) |
| `voisphon` | Nombre de voisins phonologiques |
| `puorth` | Point d'unicité orthographique |
| `puphon` | Point d'unicité phonologique |
| `old20` | Distance orthographique moyenne aux 20 mots les plus proches |
| `pld20` | Distance phonologique moyenne aux 20 mots les plus proches |

## Homographes et homophones

| Colonne | Description |
|---|---|
| `nbhomogr` | Nombre d'homographes (même orthographe, sens différent) |
| `nbhomoph` | Nombre d'homophones (même prononciation) |
| `cgramortho` | Toutes les catégories grammaticales possibles pour cette orthographe |

## Morphologie

| Colonne | Description | Exemple |
|---|---|---|
| `morphoder` | Forme de base pour la dérivation morphologique | `manger` |
| `nbmorph` | Nombre de morphèmes | `2` |

## Familiarité

| Colonne | Description |
|---|---|
| `deflem` | % de personnes connaissant la définition du lemme |
| `defobs` | Nombre d'observations pour `deflem` |
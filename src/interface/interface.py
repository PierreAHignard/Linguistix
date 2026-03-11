import gradio as gr
#from core.game_state import GameState
#from api.claude_client import ClaudeClient


# --- FONCTIONS DE NAVIGATION ---

def start_game(mode, level, language):
    # Ici, tu initialises ton GameState avec les sélections
    # Retourne la visibilité des colonnes/groupes
    return gr.update(visible=False), gr.update(visible=True), f"Mode: {mode} | Niv: {level} | Langue: {language}"


def finish_game(current_history):
    # Supposons que tu récupères ces infos de ton objet GameState
    mot_cible = "APPLE"
    nb_essais = len(current_history)  # Nombre d'échanges dans le chatbot
    score_final = 85  # Un score calculé par ta logique

    # On prépare le texte pour le Markdown
    recap_texte = f"""
    ## Résumé de la partie
    - **Mot à trouver :** {mot_cible}
    - **Nombre d'essais :** {nb_essais}
    - **Statut :** Terminé avec succès !
    """

    # On prépare les données pour le Label (dictionnaire {Nom: Valeur})
    stats_data = {"Score Précision": score_final / 100}

    # On cache la page chat (visible=False) et on affiche la page résultat (visible=True)
    return gr.update(visible=False), gr.update(visible=True), recap_texte, stats_data


def restart_to_menu():
    return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)


# --- INTERFACE ---

with gr.Blocks() as demo:
    # 1. PAGE D'ACCUEIL
    with gr.Column(visible=True) as home_page:
        gr.Markdown("# 📚 Linguistix\n\n")
        mode = gr.Radio(["Mémoire", "Apprentissage", "Jeu"], label="Choisir un mode", value="Apprentissage")
        lang = gr.Dropdown(["Anglais", "Espagnol", "Allemand", "Japonais"], label="Langue", value="Anglais")
        diff = gr.Slider(1, 3, step=1, label="Difficulté")

        btn_start = gr.Button("Lancer la partie", variant="primary")

    # 2. PAGE CHATBOT
    with gr.Column(visible=False) as chat_page:
        game_info = gr.Markdown("Paramètres en cours...")
        chatbot = gr.Chatbot(height=400)
        msg = gr.Textbox(placeholder="Entrez votre réponse ici...")

        with gr.Row():
            btn_stop = gr.Button("Terminer la partie", variant="stop")
            clear = gr.ClearButton([msg, chatbot])

    # 3. PAGE RÉSULTATS
    with gr.Column(visible=False) as result_page:
        gr.Markdown("# 🎉 Fin de partie")

        # Ce composant recevra le texte récapitulatif
        result_display = gr.Markdown()

        # Ce composant affichera une barre de score ou un badge
        stats_display = gr.Label(label="Performance")

        with gr.Row():
            btn_replay = gr.Button("Refaire une partie")
            btn_menu = gr.Button("Retour au menu principal")

    # --- LOGIQUE DES BOUTONS ---

    # Lancer le jeu
    btn_start.click(
        start_game,
        inputs=[mode, diff, lang],
        outputs=[home_page, chat_page, game_info]
    )

    # Terminer le jeu (vers résultats)
    btn_stop.click(
        finish_game,
        inputs=[chatbot],  # On prend l'état actuel du chat pour compter les essais
        outputs=[chat_page, result_page, result_display, stats_display]
    )

    # Navigation retour
    btn_menu.click(restart_to_menu, outputs=[home_page, chat_page, result_page])
    btn_replay.click(start_game, inputs=[mode, diff, lang], outputs=[result_page, chat_page, game_info])


    # Logique du Chat (simplifiée)
    def chat_logic(user_message, history):
        # Appelle ton api/claude_client.py ici
        bot_response = "Réponse simulée de Claude"
        return "", history + [[user_message, bot_response]]


    msg.submit(chat_logic, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(theme="soft")
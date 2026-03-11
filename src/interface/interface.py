import gradio as gr


# --- FONCTIONS DE NAVIGATION ---

def start_game(mode, level, language):
    return gr.update(visible=False), gr.update(
        visible=True), f"### 🎮 Mode: {mode} | Niveau: {level} | Langue: {language}"


def finish_game(current_history):
    # current_history est une liste de dicts : [{"role": "user", "content": "..."}, ...]
    mot_cible = "APPLE"

    # On compte le nombre de messages de l'utilisateur pour avoir le nombre d'essais
    nb_essais = len([m for m in current_history if m['role'] == 'user'])
    score_final = 85

    recap_texte = f"""
## 🎉 Fin de partie
- **Mot à trouver :** {mot_cible}
- **Nombre d'essais :** {nb_essais}
- **Statut :** Terminé avec succès !
    """
    stats_data = {"Score Précision": score_final / 100}

    return gr.update(visible=False), gr.update(visible=True), recap_texte, stats_data


def restart_to_menu():
    return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)


# --- INTERFACE ---

# On enlève theme="soft" d'ici pour Gradio 6.0
with gr.Blocks() as demo:
    # 1. PAGE D'ACCUEIL
    with gr.Column(visible=True) as home_page:
        gr.Markdown("# 📚 Linguistix")
        mode = gr.Radio(["Mémoire", "Apprentissage", "Jeu"], label="Choisir un mode", value="Apprentissage")
        lang = gr.Dropdown(["Anglais", "Espagnol", "Allemand", "Japonais"], label="Langue", value="Anglais")
        diff = gr.Slider(1, 3, step=1, label="Difficulté")
        btn_start = gr.Button("Lancer la partie", variant="primary")

    # 2. PAGE CHATBOT
    with gr.Column(visible=False) as chat_page:
        game_info = gr.Markdown("Paramètres en cours...")
        # Pas de type="messages", c'est le défaut en v6
        chatbot = gr.Chatbot(height=400)
        msg = gr.Textbox(placeholder="Entrez votre réponse ici...")

        with gr.Row():
            btn_stop = gr.Button("Terminer la partie", variant="stop")
            clear = gr.ClearButton([msg, chatbot])

    # 3. PAGE RÉSULTATS
    with gr.Column(visible=False) as result_page:
        result_display = gr.Markdown()
        stats_display = gr.Label(label="Performance")

        with gr.Row():
            btn_menu = gr.Button("Retour au menu principal")

    # --- LOGIQUE DES BOUTONS ---

    btn_start.click(
        start_game,
        inputs=[mode, diff, lang],
        outputs=[home_page, chat_page, game_info]
    )

    btn_stop.click(
        finish_game,
        inputs=[chatbot],
        outputs=[chat_page, result_page, result_display, stats_display]
    )

    btn_menu.click(restart_to_menu, outputs=[home_page, chat_page, result_page])


    # --- LOGIQUE DU CHAT (FORMAT DICT POUR GRADIO 6) ---
    def chat_logic(user_message, history):
        if history is None:
            history = []

        # Format attendu par Gradio 5/6
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": "Réponse simulée de Claude"})

        return "", history


    msg.submit(chat_logic, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    # On passe le thème ici pour respecter la nouvelle API
    demo.launch(theme="soft")
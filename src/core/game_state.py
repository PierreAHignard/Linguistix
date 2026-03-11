from config.modes import MODES, LEVEL, MODE_CONFIG
from config.dictionary import DICTIONARY
from utils.logger import get_logger

class GameStateParameters:
    def __init__(self, logger):
        self.mode = MODES[0]
        self.language = DICTIONARY.keys[0]
        self.questions_allowed = MODE_CONFIG[self.mode][1]["questions_allowed"]
        self.target_language_only = MODE_CONFIG[self.mode][1]["target_language_only"]

        self.logger = logger

    def update_parameters(self, mode, level, language):
        """
        Updates GameState.parameters attributes according to new game parameters.

        :param mode: Game mode ("memory", "learning", "game")
        :param level: Game difficulty level [1, 3]
        :param language: Game language

        :return: A tuple (success status, error message).
        :rtype: tuple[bool, str | None]
        """
        # Mode
        if mode not in MODES:
            self.logger.error(f"Mode {mode} not recognised. Used default (or previous) value instead.")
        else:
            self.mode = mode

        # Difficulty level-specific parameters
        if level not in LEVEL:
            self.logger.error(f"Level {level} not recognised. Used default (or previous) value instead.")
        else:
            self.questions_allowed = MODE_CONFIG[self.mode][level]["questions_allowed"]
            self.target_language_only = MODE_CONFIG[self.mode][level]["target_language_only"]

        # Language
        if language not in DICTIONARY.keys:
            self.logger.error(f"Language {language} not recognised. Used default (or previous) value instead.")
        else:
            self.language = language

class GameStateCurrent:
    def __init__(self, logger):
        self.tries_history = []
        self.response_history = []

        self.help_history = []

        self.logger = logger

    def add_word_attempt(self, word, response):
        self.tries_history.append(word)

    @property
    def tries_number(self):
        return len(self.tries_history)

class GameState:
    """
    Global GamsState class, holds all parameters, current_state values...
    """
    def __init__(self):
        # Other utils
        self.logger = get_logger()

        # Game Parameters attributes
        self.parameters = GameStateParameters(self.logger)

        # Game current state attributes
        self.current_state = GameStateCurrent(self.logger)

        # Target word
        self.target_word = str

    def update_parameters(self, mode, level, language):
        """
        Updates GameState.parameters attributes according to new game parameters.

        :param mode: Game mode ("memory", "learning", "game")
        :param level: Game difficulty level [1, 3]
        :param language: Game language

        :return: A tuple (success status, error message).
        :rtype: tuple[bool, str | None]
        """
        return self.parameters.update_parameters(mode, level, language)

    def add_word_attempt(self, word, response):
        self.current_state.add_word_attempt(word, response)

    def set_target_word(self, word):
        self.target_word = word

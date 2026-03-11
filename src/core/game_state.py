from config.modes import MODES, LEVEL, MODE_CONFIG, SUPPORTED_LANGUAGES
from utils.logger import get_logger

class GameStateParameters:
    def __init__(self, logger):
        self.mode = MODES[0]
        self.language = SUPPORTED_LANGUAGES[0]
        self.questions_allowed = MODE_CONFIG[self.mode][1]["questions_allowed"]
        self.target_language_only = MODE_CONFIG[self.mode][1]["target_language_only"]

        self._logger = logger

    def update(self, mode, level, language):
        """
        Updates GameState.parameters attributes according to new game parameters.

        :param mode: Game mode ("memory", "learning", "game")
        :param level: Game difficulty level [1, 3]
        :param language: Game language

        :return: A tuple (success status, error message).
        :rtype: tuple[bool, str | None]
        """
        if mode not in MODES:
            self._logger.error(f"Mode {mode} not recognised. Used default (or previous) value instead.")
        else:
            self.mode = mode

        if level not in LEVEL:
            self._logger.error(f"Level {level} not recognised. Used default (or previous) value instead.")
        else:
            self.questions_allowed = MODE_CONFIG[self.mode][level]["questions_allowed"]
            self.target_language_only = MODE_CONFIG[self.mode][level]["target_language_only"]

        if language not in SUPPORTED_LANGUAGES:
            self._logger.error(f"Language {language} not recognised. Used default (or previous) value instead.")
        else:
            self.language = language

class GameStateCurrent:
    def __init__(self, logger):
        self.tries_history = []
        self.number_tries = 0

        self.help_history = []

        self.logger = logger

class GameState:
    def __init__(self):
        # Other utils
        self.logger = get_logger()

        # Game Parameters attributes
        self.parameters = GameStateParameters(self.logger)

        # Game current state attributes
        self.current_state = GameStateCurrent(self.logger)



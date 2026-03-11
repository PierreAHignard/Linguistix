MODES = ["memory", "learning", "game"]

LEVEL = [1,2,3]

MODE_CONFIG = {
    "memory": { # Definition first
        1: {"questions_allowed": True,  "target_language_only": True},
        2: {"questions_allowed": False, "target_language_only": True},
    },
    "learning": {
        1: {"questions_allowed": True,  "target_language_only": False},
        2: {"questions_allowed": True,  "target_language_only": True},
        3: {"questions_allowed": True,  "target_language_only": True,  "strict_language": True},
    },
    "game": { # No definition, nothing to begin
        1: {"questions_allowed": False, "target_language_only": True},
    },
}
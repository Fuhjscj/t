class Version:
    MAJOR = 2
    MINOR = 0
    PATCH = 0
    META = "-beta"

    @classmethod
    def str(cls):
        ver = f"{cls.MAJOR}.{cls.MINOR}.{cls.PATCH}"
        if cls.META:
            ver += f"{cls.META}"
        return ver


__version__ = Version.str()
__author__ = 'lordralinc'

config = None
CALLBACK_LINK = "https://irisduty.ru/callback/"

GITHUB_LINK = "https://github.com/lordralinc/idm_lp"
VERSION_REST = "https://raw.githubusercontent.com/LordRalInc/idmmulti_lp-rest/master/version.json"
ALIASES_REST = "https://raw.githubusercontent.com/LordRalInc/idmmulti_lp-rest/master/aliases.json"
ROLE_PLAY_COMMANDS_REST = "https://raw.githubusercontent.com/LordRalInc/idmmulti_lp-rest/master/role_play_commands.json"
ROLE_PLAY_COMMANDS_USE_REST = True

ENABLE_EVAL = False
ALLOW_SENTRY = True
SENTRY_URL = "https://7a3f1b116c67453c91600ad54d4b7087@o481403.ingest.sentry.io/5529960"

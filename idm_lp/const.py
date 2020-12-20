class Version:
    MAJOR = 2
    MINOR = 2
    PATCH = 0
    META = "-beta"

    def __init__(
            self,
            major: int = None,
            minor: int = None,
            patch: int = None,
            meta: str = None
    ):
        self.MAJOR = major or self.MAJOR
        self.MINOR = minor or self.MINOR
        self.PATCH = patch or self.PATCH
        self.META = meta or self.META

    def str(self):
        ver = f"{self.MAJOR}.{self.MINOR}.{self.PATCH}"
        if self.META:
            ver += f"{self.META}"
        return ver

    def do_func(self, func, other: 'Version'):
        if not isinstance(other, Version):
            raise ValueError("Only Version class")
        if func(self.MAJOR, other.MAJOR):
            return True
        if func(self.MINOR, other.MINOR):
            return True
        if func(self.PATCH, other.PATCH):
            return True
        return False

    def __gt__(self, other: 'Version') -> bool:
        return self.do_func(int.__gt__, other)

    def __lt__(self, other: 'Version') -> bool:
        return self.do_func(int.__lt__, other)

    def __ge__(self, other: 'Version') -> bool:
        return self.do_func(int.__ge__, other)

    def __le__(self, other: 'Version') -> bool:
        return self.do_func(int.__le__, other)


__version__ = Version().str()
__author__ = 'lordralinc'

config = None
CALLBACK_LINK = "https://irisduty.ru/callback/"

GITHUB_LINK = "https://github.com/lordralinc/idm_lp"
VERSION_REST = "https://raw.githubusercontent.com/lordralinc/idm_lp-rest/main/manifest.json"
ALIASES_REST = "https://raw.githubusercontent.com/LordRalInc/idmmulti_lp-rest/master/aliases.json"
ROLE_PLAY_COMMANDS_REST = "https://raw.githubusercontent.com/LordRalInc/idmmulti_lp-rest/master/role_play_commands.json"
ROLE_PLAY_COMMANDS_USE_REST = True

ENABLE_EVAL = False
ALLOW_SENTRY = True
SENTRY_URL = "https://7a3f1b116c67453c91600ad54d4b7087@o481403.ingest.sentry.io/5529960"

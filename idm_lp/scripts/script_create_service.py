import sys
from gettext import gettext as _

from . import utils


def heroku_deploy(base_dir: str):
    utils.clear()
    if sys.platform.startswith("win"):
        print(_("Не доступно для WINDOWS..."))
        return

    utils.print_menu_item()


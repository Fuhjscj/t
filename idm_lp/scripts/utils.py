import os
import sys
from os import isatty


def print_menu_item(label: str, message: str, active: bool = False):
    print("{active: <4} {label} {message}".format(label=label, message=message, active="-->" if active else ""))


def clear():
    if not isatty(sys.stdout):
        return
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        sys.stdout.write("\033[2J\033[1;1H")

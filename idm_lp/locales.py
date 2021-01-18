import argparse
import gettext
import locale
import os
from configparser import ConfigParser
from gettext import gettext as _

import requests
from tortoise import Tortoise
from vkbottle import User

from . import const, utils
from .commands import blueprints

base_dir = os.path.dirname(__file__)
lang_dir = os.path.join(base_dir, 'lang')

SETTINGS = {
    'locales': {
        'en': 'en_US',
        'ru': 'ru_RU'
    },
    'locale': 'ru_RU',
}


# INIT LOCALES
def __translate_standard_messages():
    """Эта функция нужна только для того, чтобы Poedit при сканировании
       добавлял соответствующие строки в .po-файл для их перевода.
       Строки скопированы из стандартного модуля Python argparse.py.
    """
    # argparse
    _('%(prog)s: error: %(message)s\n')
    _('expected one argument')
    _('invalid choice: %(value)r (choose from %(choices)s)')
    _('not allowed with argument %s')
    _('optional arguments')
    _('positional arguments')
    _('show this help message and exit')
    _('usage: ')


def _get_locale():
    _locale, _encoding = locale.getdefaultlocale()  # Значения по умолчанию

    parser = argparse.ArgumentParser(add_help=False)
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-l', '--lang', choices=list(SETTINGS['locales']),
        default=None, help='Language to use.'
    )

    group.add_argument(
        '--locale', choices=list(SETTINGS['locales'].values()),
        default=_locale, help='Locale to use.'
    )

    # Не будет ругаться на неизвестные параметры
    args, _ignore = parser.parse_known_args()

    if args.lang:
        return SETTINGS['locales'][args.lang]
    else:  # У этого параметра всегда будет значение по умолчанию
        return args.locale


_locale = _get_locale()
locale.setlocale(locale.LC_ALL, _locale)
os.environ['LANGUAGE'] = _locale
gettext.textdomain('idm_lp')
gettext.bindtextdomain('idm_lp', lang_dir)

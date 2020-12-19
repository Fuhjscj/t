import argparse
import gettext
import locale
from configparser import ConfigParser
from gettext import gettext as _
import os

import requests
from tortoise import Tortoise

from vkbottle import User

from .commands import blueprints
from . import const, utils

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


def startup_message(_user: User):
    async def wrapper():
        text = _(
            "IDM LP by %(author)s запущен\n"
            "Текущая версия: v%(version)s\n"
        ) % dict(
            version=const.__version__,
            author=const.__author__
        )
        version_rest = requests.get(const.VERSION_REST).json()
        cloud_version = const.Version(**version_rest['version'])
        if cloud_version > const.Version():
            text += _(
                "Доступно обновление %(version)s\n%(github_url)s"
            ) % dict(
                version=cloud_version.str(),
                github_url=const.GITHUB_LINK
            )
        await user.api.messages.send(
            peer_id=await user.api.user_id,
            random_id=0,
            message=text
        )
    return wrapper


def init_database(url: str):
    async def init():
        await Tortoise.init(
            db_url=url,
            modules={'models': ['idm_lp.models']}
        )
        await Tortoise.generate_schemas()
        await utils.temp.AliasTemp.load_from_db()
        await utils.temp.RolePlayCommandTemp.load_from_db()

    return init


def startup(_user: User, _database_url: str):
    async def wrapper():
        await init_database(_database_url)()
        await startup_message(_user)()

    return wrapper


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


def _parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-l', '--lang', choices=list(SETTINGS['locales']),
        help=_('Language to use.')
    )
    group.add_argument(
        '--locale', choices=list(SETTINGS['locales'].values()),
        help=_('Locale to use.')
    )


_locale = _get_locale()
locale.setlocale(locale.LC_ALL, _locale)
os.environ['LANGUAGE'] = _locale
gettext.textdomain('idm_lp')
gettext.bindtextdomain('idm_lp', lang_dir)

parser = argparse.ArgumentParser(
    description=_(
        'LP модуль позволяет работать приемнику сигналов «IDM multi» работать в любых чатах.\n'
        'Так же он добавляет игнор, глоигнор, мут и алиасы.'
    ),
    prog='python3 -m idm_lp',
    add_help=False
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    '-l', '--lang', choices=list(SETTINGS['locales']),
    help=_('Language to use.')
)
group.add_argument(
    '--locale', choices=list(SETTINGS['locales'].values()),
    help=_('Locale to use.')
)
subparsers = parser.add_subparsers(title='action', help=_('Вариант запуска'))

script_parser = subparsers.add_parser('utils', help=_('Скрипты помощи'))
start_parser = subparsers.add_parser('start', help=_('Запуск скрипта'))

script_name = script_parser.add_argument('script_name', help=_('Имя скрипта'))

start_parser.add_argument(
    '--config_path',
    default='config.ini',
    action='store',
    type=str,
    help=_('Путь до конфига')
)
start_parser.add_argument(
    '--vkbottle-logger-level',
    default='INFO',
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    action='store',
    type=str,
    help=_('Уровень логгирования vkbottle')
)
start_parser.add_argument(
    '--vkbottle-logger-file-path',
    default='logs/vkbottle.log',
    action='store',
    type=str,
    help=_('Путь до файла с логами vkbottle')
)

args = parser.parse_args()

if hasattr(args, 'script_name'):
    from . import utils, const

    if hasattr(utils, args.script_name):
        getattr(utils, args.script_name)(base_dir)
    else:
        print(_("Скрипт %s не найден" % args.script_name))
    exit(1)

if hasattr(args, 'config_path'):
    config = ConfigParser()
    config.read(args.config_path, encoding='utf-8')
    const.config = config

    database_url = "mysql://%(user)s:%(password)s@%(host)s:3306/%(database)s" % config['Database']
    from .validators import *

    user = User(
        tokens=config['User']['tokens'].split(","),
        log_to_path=args.vkbottle_logger_file_path,
        debug=args.vkbottle_logger_level
    )
    user.set_blueprints(*blueprints)
    user.run_polling(
        on_startup=startup(user, database_url)
    )

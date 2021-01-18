import argparse
import os
from gettext import gettext as _

base_dir = os.path.dirname(__file__)
lang_dir = os.path.join(base_dir, 'lang')

SETTINGS = {
    'locales': {
        'en': 'en_US',
        'ru': 'ru_RU'
    },
    'locale': 'ru_RU',
}


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

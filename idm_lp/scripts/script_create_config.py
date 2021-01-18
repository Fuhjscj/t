import os
from gettext import gettext as _
from typing import List
from . import utils
from .utils import print_menu_item


def get_tokens() -> List[str]:
    utils.clear()
    print_menu_item("1. ", _("Настройка токенов"), True)
    print_menu_item("2. ", _("Настройка секретного кода IDM"))
    print_menu_item("3. ", _("Настройка базы данных"))

    print("_" * 10)

    print(_("Настройка токенов."))
    print(_("Получить тожно тут: https://vkhost.github.io/"))
    tokens = []
    while True:
        token = input(
            _("Введите токен (85 символов. Для для того чтобы перейти к следующему пункту введите 0) > ")
        )
        if token == "0":
            break
        if len(token) != 85:
            print("Токен должен быть длинной 85 символов")
            continue
        tokens.append(token)
    return tokens


def get_secret_code() -> str:
    utils.clear()
    print_menu_item("1. ", _("Настройка токенов"))
    print_menu_item("2. ", _("Настройка секретного кода IDM"), True)
    print_menu_item("3. ", _("Настройка базы данных"))
    print("_" * 10)

    print(_("Настройка секретного кода IDM"))
    secret_code = input(
        _("Введите секретный код IDM (Узнать можно в панели дежурного) > ")
    )
    return secret_code


def get_database_url() -> str:
    utils.clear()
    print_menu_item("1. ", _("Настройка токенов"))
    print_menu_item("2. ", _("Настройка секретного кода IDM"))
    print_menu_item("3. ", _("Настройка базы данных"), True)
    print("_" * 10)

    print(_("Настройка базы данных"))
    print(_("1 - ввести URL базы данных"))
    print(_("2 - ввести реквезиты базы данных MySQL"))
    database_scheme = input("> ")
    if database_scheme == '1':
        database_url = input("URL > ")
    else:
        host = input("HOST > ")
        user = input("USER > ")
        password = input("PASSWORD > ")
        database = input("DATABASE > ")
        database_url = "mysql://%(user)s:%(password)s@%(host)s:3306/%(database)s" % dict(
            host=host,
            user=user,
            password=password,
            database=database
        )
    return database_url


def create_config(base_dir: str):
    tokens = get_tokens()
    secret_code = get_secret_code()
    database_url = get_database_url()

    config_str = """[User]
tokens=%(tokens)s
secret_code=%(secret_code)s

[Prefixes]
service=!слп,.слп
duty=!лд,.лд
self=!л,.л

[Database]
db_url=%(db_url)s
host=
user=
password=
database=
""" % dict(
        tokens=",".join(tokens),
        secret_code=secret_code,
        db_url=database_url
    )
    with open('config.ini', 'w', encoding='utf-8') as f:
        f.write(config_str)
    utils.clear()
    print(_("Конфиг записан, путь до файла: %s") % os.path.abspath("config.ini"))

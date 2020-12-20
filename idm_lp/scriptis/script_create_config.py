import os
from gettext import gettext as _


def create_config(base_dir: str):
    print("_____________")
    print(_("Настройка токенов."))
    print("_____________")
    print(_("Получить тожно тут: https://vkhost.github.io/"))
    print("_____________")
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
    print("_____________")
    print(_("Настройка секретного кода IDM"))
    secret_code = input(
        _("Введите секретный код IDM (Узнать можно в панели дежурного) > ")
    )

    print("_____________")
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
    print(_("Конфиг записан, путь до файла: %s") % os.path.abspath("config.ini"))

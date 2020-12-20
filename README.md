# IDM multi - LP module
![Version](https://img.shields.io/badge/dynamic/json?color=blue&label=version&query=%24.version_str&url=https%3A%2F%2Fraw.githubusercontent.com%2Flordralinc%2Fidm_lp-rest%2Fmain%2Fmanifest.json)
![GitHub](https://img.shields.io/github/license/lordralinc/idm_lp)
![GitHub repo size](https://img.shields.io/github/repo-size/lordralinc/idm_lp)

LP модуль позволяет работать приемнику сигналов «IDM multi» работать в любых чатах.
Так же он добавляет игнор, глоигнор, мут и алиасы.

[История изменений](https://github.com/lordralinc/idm_lp/blob/2.0/CHANGELOG.md)

<!--
4: 252535322122234232
  1  2  3  4  5
1 a  b  c  d  e
2 f  g  h  ij k
3 l  m  n  o  p
4 q  r  s  y  u
5 v  w  x  y  z
-->

## Установка
```shell script
pip install https://github.com/lordralinc/idm_lp/archive/2.0.zip
```

## Запуск
```shell script
# Запуск утилит: 
python3 -m idm_lp [-l lang | --locale locale] utils {script_name}
```
| Переменная  | Описание      | Доступные параметры |
|-------------|---------------|---------------------|
| lang        | язык          | en, ru              |
| locale      | локаль        | en\_US, ru\_RU      |
| script_name | имя скрипта   | en\_US, ru\_RU      |
```shell script
# Запуск ЛП
python3 -m idm_lp start [-h] [--config_path CONFIG_PATH] [--vkbottle-logger-level LOG_LEVEL] [--vkbottle-logger-file-path VKBOTTLE_LOGGER_FILE_PATH]
```
| Переменная                   | Описание                        | Доступные параметры                   |
|------------------------------|---------------------------------|---------------------------------------|
| CONFIG\_PATH                 | Путь до конфига                 |                                       |
| LOG\_LEVEL                   | Уровень логгирования vkbottle   | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| VKBOTTLE\_LOGGER\_FILE\_PATH | Путь до файла с логами vkbottle |                                       |

# Список скриптов
| Имя скрипта    | Описание       |
|----------------|----------------|
| create\_config | Создает конфиг |

## Команды
| Префикс   | Имя             | Аргументы                                 | Описание                                         |
|-----------|-----------------|-------------------------------------------|--------------------------------------------------|
| свой      |                 | \[команда к IDM\]                         | Выполняет запрос на исполнение команды к IDM     |
| дежурный  |                 | \[пуш на юзера\] \[команда к IDM\]        | Выполняет запрос на исполнение команды к IDM     |
| сервисный | пинг, кинг, пиу | подробно                                  | Показывает пинг                                  |
| сервисный | инфо            |                                           | Показывает информацию о модуле                   |
| сервисный | \+алиас         | \[имя\]\\n\[команда\]\\n\[команда к IDM\] | Добавляет алиас                                  |
| сервисный | \-алиас         | \[имя\]                                   | Удаляет алиас                                    |
| сервисный | алиасы          |                                           | Показывает все алиасы                            |
| сервисный | алиасы обновить |                                           | Обновляет алиасы в памяти из базы данных         |
| сервисный |                 | \[РП\-команда\] \[\{пуш\}\|\{всех\}\]     | Вызывает РП\-команду                             |
| сервисный | рп              |                                           | Показывает список РП                             |
| сервисный | рп обновить     |                                           | Обновляет РП\-команды в памяти из базы данных    |
| сервисный | рп загрузить    | \[URL к РП\-командам\]                    | Добавляет в БД РП\-команды                       |
| сервисный |  \-рп           | \[имя\]                                   | Удаляет РП\-команду                              |

## Полезные ссылки
| URL                                         | Описание                           |
|---------------------------------------------|------------------------------------|
| [remotemysql.com](https://remotemysql.com/) | Бесплатный хост для MySQL          |
| [heroku.com](https://www.heroku.com/)       | Бесплатный хост (есть ограничения) |




import os
from gettext import gettext as _

from vkbottle import User

base_dir = os.path.dirname(__file__)
lang_dir = os.path.join(base_dir, 'lang')

SETTINGS = {
    'locales': {
        'en': 'en_US',
        'ru': 'ru_RU'
    },
    'locale': 'ru_RU',
}


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
                "Доступно обновление %(version)s\n История изменений: %(changelog_url)s\n%(github_url)s"
            ) % dict(
                version=cloud_version.str(),
                changelog_url=const.CHANGELOG_LINK,
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


from .locales import *
from .arguments_parser import *

args = parser.parse_args()

if hasattr(args, 'script_name'):
    from . import scriptis, const

    if hasattr(scriptis, args.script_name):
        getattr(scriptis, args.script_name)(base_dir)
    else:
        print(_("Скрипт %s не найден" % args.script_name))
    exit(1)

if hasattr(args, 'config_path'):
    config = ConfigParser()
    config.read(args.config_path, encoding='utf-8')
    const.config = config
    if config['Database'].get('db_url', None):
        database_url = config['Database'].get('db_url', None)
    else:
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

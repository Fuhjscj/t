import time
from typing import Tuple, Dict

from vkbottle import Message
from vkbottle.framework.blueprint.user import Blueprint

from idm_lp import const
from idm_lp.models import Alias
from idm_lp.utils import edit_message, check_ping

user = Blueprint()


async def get_delta(func, args: Tuple = None, kwargs: Dict = None):
    if args is None:
        args = tuple()
    if kwargs is None:
        kwargs = dict()

    start = time.time()
    await func(*args, **kwargs)
    return time.time() - start


async def get_ping(message: Message, answer: str) -> str:
    delta = round(time.time() - message.date, 2)

    # А ты думал тут все чесно будет? Не, я так не работаю...
    if delta < 0:
        delta = "666"

    return f"{answer} Модуль ЛП\n" \
           f"Ответ через {delta} с"


async def get_ping_detail(message: Message, answer: str) -> str:
    delta = round(time.time() - message.date, 2)
    vk = await get_delta(message.api.users.get)
    database = await get_delta(Alias.all().count)
    idm = await get_delta(check_ping, args=(const.config['User']['secret_code'],))

    # А ты думал тут все чесно будет? Не, я так не работаю...
    if delta < 0:
        delta = "666"

    return (
        f"{answer} Модуль ЛП\n"
        f"Ответ через {delta} с\n"
        f"Пинг ВК {round(vk, 2)} с\n"
        f"Пинг БД {round(database, 2)} с\n"
        f"Пинг IDM {round(idm, 2)} с"
    )


@user.on.message_handler(text="<p:prefix_service> пинг")
@user.on.message_handler(text="<p:prefix_service> пинг подробно")
async def ping_wrapper(message: Message, **kwargs):
    await edit_message(
        message,
        await get_ping(message, 'ПОНГ') if 'подробно' not in message.text else await get_ping_detail(message, 'ПОНГ')
    )


@user.on.message_handler(text="<p:prefix_service> кинг")
@user.on.message_handler(text="<p:prefix_service> кинг подробно")
async def ping_wrapper(message: Message, **kwargs):
    await edit_message(
        message,
        await get_ping(message, 'КОНГ') if 'подробно' not in message.text else await get_ping_detail(message, 'КОНГ')
    )


@user.on.message_handler(text="<p:prefix_service> пиу")
@user.on.message_handler(text="<p:prefix_service> пиу подробно")
async def ping_wrapper(message: Message, **kwargs):
    await edit_message(
        message,
        await get_ping(message, 'ПАУ') if 'подробно' not in message.text else await get_ping_detail(message, 'ПАУ')
    )

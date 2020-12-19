import time
from gettext import gettext as _
from typing import Tuple, Dict

from vkbottle import Message
from vkbottle.framework.blueprint.user import Blueprint
from vkbottle.framework.framework.rule import FromMe

from idm_lp import const
from idm_lp.models import Alias
from idm_lp.utils import edit_message, check_ping

user = Blueprint(
    name="ping_blueprint"
)


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

    return _(
        "%(answer)s Модуль ЛП\n"
        "Ответ через %(delta)s с."
    ) % dict(answer=answer, delta=str(delta))


async def get_ping_detail(message: Message, answer: str) -> str:
    delta = round(time.time() - message.date, 2)
    vk = await get_delta(message.api.users.get)
    database = await get_delta(Alias.all().count)
    idm = await get_delta(check_ping, args=(const.config['User']['secret_code'],))

    # А ты думал тут все чесно будет? Не, я так не работаю...
    if delta < 0:
        delta = "666"

    return _(
        "%(answer)s Модуль ЛП\n"
        "Ответ через %(delta)s с.\n"
        "Пинг ВК %(vk)g с.\n"
        "Пинг БД %(database)g с.\n"
        "Пинг IDM %(idm)g с."
    ) % dict(
        answer=answer,
        delta=str(delta),
        vk=round(vk, 2),
        database=round(database, 2),
        idm=round(idm, 2)
    )


@user.on.message_handler(FromMe(), text="<p:prefix_service> пинг")
@user.on.message_handler(FromMe(), text="<p:prefix_service> пинг подробно")
async def ping_wrapper(message: Message, **kwargs):
    await edit_message(
        message,
        await get_ping(message, _('ПОНГ'))
        if 'подробно' not in message.text
        else await get_ping_detail(message, _('ПОНГ'))
    )


@user.on.message_handler(FromMe(), text="<p:prefix_service> кинг")
@user.on.message_handler(FromMe(), text="<p:prefix_service> кинг подробно")
async def ping_wrapper(message: Message, **kwargs):
    await edit_message(
        message,
        await get_ping(message, _('КОНГ'))
        if 'подробно' not in message.text
        else await get_ping_detail(message, _('КОНГ'))
    )


@user.on.message_handler(FromMe(), text="<p:prefix_service> пиу")
@user.on.message_handler(FromMe(), text="<p:prefix_service> пиу подробно")
async def ping_wrapper(message: Message, **kwargs):
    await edit_message(
        message,
        await get_ping(message, _('ПАУ'))
        if 'подробно' not in message.text
        else await get_ping_detail(message, _('ПАУ'))
    )

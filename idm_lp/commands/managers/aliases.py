from gettext import gettext as _

from vkbottle import Message
from vkbottle.framework.blueprint.user import Blueprint

from idm_lp.models import Alias
from idm_lp.utils import edit_message
from idm_lp.utils.temp import AliasTemp

user = Blueprint()


@user.on.message_handler(text="<p:prefix_service> +алиас <name>\n<command_from>\n<command_to>")
async def wrapper(message: Message, name: str, command_from: str, command_to: str, **kwargs):
    name = name.lower()
    command_from = command_from.lower()
    command_to = command_to.lower()

    if AliasTemp.get_by_name(name):
        await edit_message(
            message,
            _("⚠ Алиас «%s» уже был создан") % name
        )
        return
    await AliasTemp.create(
        name=name,
        command_from=command_from,
        command_to=command_to
    )
    await edit_message(
        message,
        _("✅ Алиас «%s» был создан") % name
    )


@user.on.message_handler(text="<p:prefix_service> -алиас <name>")
async def wrapper(message: Message, name: str, **kwargs):
    name = name.lower()

    if await AliasTemp.delete(name):
        await edit_message(
            message,
            _("✅ Алиас «%s» удален") % name
        )
        return
    else:
        await edit_message(
            message,
            _("⚠ Алиас «%s» не найден") % name
        )
    await AliasTemp.load_from_db()


@user.on.message_handler(text="<p:prefix_service> алиасы")
async def wrapper(message: Message, **kwargs):
    text = _("📃 Алиасы: \n")
    index = 1
    async for alias in Alias.all():
        text += f"{index}. {alias.name} | {alias.command_from} -> !л {alias.command_to}\n"
        index += 1
    text += _("\nВсего алиасов: %d\nАлиасов в памяти: %d") % (await Alias.all().count(), len(AliasTemp.data))
    await edit_message(
        message,
        text
    )


@user.on.message_handler(text="<p:prefix_service> алиасы обновить")
async def wrapper(message: Message, **kwargs):
    await AliasTemp.load_from_db()
    await edit_message(
        message,
        _("✅ Алиасы успешно обновлены")
    )

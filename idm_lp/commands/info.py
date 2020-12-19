from gettext import gettext as _

from vkbottle import Message
from vkbottle.framework.blueprint.user import Blueprint
from vkbottle.framework.framework.rule import FromMe

from idm_lp import const, models
from idm_lp.models import Settings, EFCSchemeEnum
from idm_lp.utils import edit_message

user = Blueprint(
    name="ping_blueprint"
)


def b2s(value) -> str:
    return '✅' if value else '❌'


@user.on.message_handler(FromMe(), text="<p:prefix_service> инфо")
async def info_wrapper(message: Message, **kwargs):
    settings = await Settings.get_or_create_model()
    text = _(
        "❤ IDM LP v%(version)s by %(author)s\n"
        "▶ Язык lang\n\n"

        "▶ Ключ рукаптчи: %(ru_captcha_key)s\n\n"

        "▶ Удаление all-пушей: %(delete_all_notify)s\n"
        "▶ Удаление пушей на себя: %(delete_self_notify)s\n\n"

        "▶ Выход из бесед: %(efc_enable)s\n"
        "▶ Выход из бесед: удалять чат %(efc_delete_chat)s\n"
        "▶ Выход из бесед: блокировать пригласившего %(efc_block_sender)s\n"
        "▶ Выход из бесед: схема %(efc_scheme)s\n\n"

        "▶ В игноре: %(ignored)d\n"
        "▶ В глобальном игноре: %(ignored_global)d\n"
        "▶ В муте: %(muted)d\n\n"

        "▶ Сервисные префиксы: %(service_prefixes)s\n"
        "▶ Свои префиксы: %(self_prefixes)s\n"
        "▶ Префиксы дежурного: %(duty_prefixes)s\n"
    ) % dict(
        version=const.__version__,
        author=const.__author__,

        ru_captcha_key=b2s(settings.ru_captcha_key),

        delete_all_notify=b2s(settings.delete_all_notify),
        delete_self_notify=b2s(settings.delete_self_notify),

        efc_enable=b2s(settings.efc_enable),
        efc_delete_chat=b2s(settings.efc_delete_chat),
        efc_block_sender=b2s(settings.efc_block_sender),
        efc_scheme=_('белый список') if settings.efc_scheme == EFCSchemeEnum.WHITE_LIST else _('черный список'),

        ignored=await models.IgnoredMember.all().count(),
        ignored_global=await models.IgnoredGlobalMember.all().count(),
        muted=await models.MutedMember.all().count(),

        service_prefixes=const.config['Prefixes']['service'],
        self_prefixes=const.config['Prefixes']['self'],
        duty_prefixes=const.config['Prefixes']['duty'],
    )
    await edit_message(
        message,
        text
    )

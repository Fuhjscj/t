from typing import Optional

from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message

from idm_lp import const
from idm_lp.utils import send_request
from idm_lp.models import Alias

user = Blueprint(
    name='aliases_blueprint'
)


async def send_signal(
        message: Message,
        alias: Alias,
        separator: str = ' ',
        signal: Optional[str] = None
):
    message_data = message.dict()
    prepared_text = const.config['Prefixes']['self'].split(',')[0] + ' ' + alias.command_to
    prepared_text += f"{separator}{signal}" if signal else ''

    request_data = {
        "user_id": message_data['from_id'],
        "method": "lpSendMySignal",
        "secret": const.config['User']['secret_code'],
        "message": {
            "conversation_message_id": message_data['conversation_message_id'],
            "from_id": message_data['from_id'],
            "date": message.date,
            "text": prepared_text,
            "peer_id": message.peer_id
        },
        "object": {
            "chat": None,
            "from_id": message_data['from_id'],
            "value": prepared_text,
            "conversation_message_id": message_data['conversation_message_id']
        },
        "vkmessage": message_data
    }
    await send_request(request_data)


@user.on.message_handler(FromMe(), text=['<alias:alias> <signal>', '<alias:alias>'])
async def duty_signal(message: Message, alias: Alias, signal: str = None):
    await send_signal(message, alias, ' ', signal)


@user.on.message_handler(FromMe(), text='<alias:alias>\n<signal>')
async def duty_signal_new_line(message: Message, alias: Alias, signal: str):
    await send_signal(message, alias, '\n', signal)

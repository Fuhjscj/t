from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message

from idm_lp import const
from idm_lp.utils import send_request

user = Blueprint(
    name='self_signal_blueprint'
)


@user.on.message_handler(FromMe(), text='<prefix:prefix_self> <signal>')
async def self_signal(message: Message, prefix: str, signal: str):
    message_ = message.dict()
    __model = {
        "user_id": message_['from_id'],
        "method": "lpSendMySignal",
        "secret": const.config['User']['secret_code'],
        "message": {
            "conversation_message_id": message_['conversation_message_id'],
            "from_id": message_['from_id'],
            "date": message.date,
            "text": message.text,
            "peer_id": message.peer_id
        },
        "object": {
            "chat": None,
            "from_id": message_['from_id'],
            "value": prefix + ' ' + signal,
            "conversation_message_id": message_['conversation_message_id']
        },
        "vkmessage": message_
    }

    await send_request(__model)

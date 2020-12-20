from vkbottle.user import Blueprint, Message

from idm_lp import const
from idm_lp.utils import send_request

user = Blueprint(
    name='duty_signal_blueprint'
)


@user.on.message_handler(text='<p:prefix_duty> [id<user_id:int>|<name>] <signal>')
async def duty_signal(message: Message, prefix: str, user_id: int, signal: str, **kwargs):
    if user_id != await message.api.user_id:
        return
    message_ = message.dict()
    __model = {
        "user_id": await message.api.user_id,
        "method": "lpSendSignal",
        "secret": const.config['User']['secret_code'],
        "message": {
            "conversation_message_id": message_['conversation_message_id'],
            "from_id": message_['from_id'],
            "date": message.date,
            "text": prefix + ' ' + signal,
            "peer_id": message.peer_id
        },
        "object": {
            "chat": None,
            "from_id": message_['from_id'],
            "value": signal,
            "conversation_message_id": message_['conversation_message_id']
        },
        "vkmessage": message_
    }
    await send_request(__model)

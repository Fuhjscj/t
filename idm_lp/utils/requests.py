import aiohttp
from vkbottle.api import UserApi
from vkbottle.utils import logger

from idm_lp import const

session: aiohttp.ClientSession = aiohttp.ClientSession()


async def send_request(request_data: dict):
    logger.debug(f"Send request to server with data: {request_data}")
    global session
    api = UserApi.get_current()

    if session.closed:
        session = aiohttp.ClientSession()

    message = ""
    async with session.post(const.CALLBACK_LINK, json=request_data) as resp:
        if resp.status != 200:
            message = f"⚠ Ошибка сервера IDM Multi. Сервер, ответил кодом {resp.status}."
        else:
            data_json = await resp.json()
            if data_json['response'] == 'ok':
                return
            elif data_json['response'] == "error":
                if data_json.get('error_code') == 1:
                    message = f"⚠ Ошибка сервера IDM Multi. Сервер, ответил: <<Пустой запрос>>"
                elif data_json.get('error_code') == 2:
                    message = f"⚠ Ошибка сервера IDM Multi. Сервер, ответил: <<Неизвестный тип сигнала>>"
                elif data_json.get('error_code') == 3:
                    message = f"⚠ Ошибка сервера IDM Multi. Сервер, ответил: <<Пара пользователь/секрет не найдены>>"
                elif data_json.get('error_code') == 4:
                    message = f"⚠ Ошибка сервера IDM Multi. Сервер, ответил: <<Беседа не привязана>>"
                elif data_json.get('error_code') == 10:
                    message = f"⚠ Ошибка сервера IDM Multi. Сервер, ответил: <<Не удалось связать беседу>>"
                else:
                    message = f"⚠ Ошибка сервера IDM Multi. Сервер, ответил: <<Ошибка #{data_json.get('error_code')}>>"
            elif data_json['response'] == "vk_error":
                message = f"⚠ Ошибка сервера IDM Multi. Сервер, ответил: <<Ошибка VK #{data_json.get('error_code')} " \
                          f"{data_json.get('error_message', '')}>>"
    if message:
        await api.messages.send(
            random_id=0,
            peer_id=await api.user_id,
            message=message
        )


async def check_ping(secret_code: str):
    await send_request({
        "user_id": await UserApi.get_current().user_id,
        "method": "ping",
        "secret": secret_code,
        "message": {},
        "object": {}
    })

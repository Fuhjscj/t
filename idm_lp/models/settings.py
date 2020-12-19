from enum import Enum
from typing import Type

from tortoise import Model, fields
from tortoise.models import MODEL


class EFCSchemeEnum(Enum):
    WHITE_LIST = 'w'
    BLACK_LIST = 'b'


class Settings(Model):
    ru_captcha_key = fields.TextField(null=True)

    delete_all_notify = fields.BooleanField(default=False)
    delete_self_notify = fields.BooleanField(default=False)

    efc_enable = fields.BooleanField(default=False)
    efc_delete_chat = fields.BooleanField(default=False)
    efc_block_sender = fields.BooleanField(default=False)
    efc_scheme = fields.CharEnumField(EFCSchemeEnum, default=EFCSchemeEnum.BLACK_LIST)
    efc_black_list = fields.TextField(default="")
    efc_white_list = fields.TextField(default="")

    @classmethod
    async def get_or_create_model(
        cls: Type[MODEL],
    ) -> MODEL:
        model = await cls.first()
        if model is None:
            model = await cls.create()
        return model

    class Meta:
        table = "settings"

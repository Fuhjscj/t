from typing import Type

from pydantic import BaseModel
from tortoise import Model, fields


class Alias(Model):
    name = fields.CharField(max_length=512, unique=True)
    command_from = fields.TextField()
    command_to = fields.TextField()

    class Meta:
        table = "aliases"


class AliasPydantic(BaseModel):
    name: str
    command_from: str
    command_to: str

    @classmethod
    def load(cls: Type['AliasPydantic'], model: Alias) -> 'AliasPydantic':
        return cls(
            name=model.name,
            command_from=model.command_from,
            command_to=model.command_to
        )

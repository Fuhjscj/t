from enum import Enum
from typing import Type

from pydantic import BaseModel
from tortoise import Model, fields


class RolePlayCommandGenEnum(Enum):
    NOM = "nom"
    GEN = "gen"
    DAT = "dat"
    ACC = "acc"
    INS = "ins"
    ABL = "abl"


class RolePlayCommand(Model):
    name = fields.CharField(max_length=512, unique=True)
    gen = fields.CharEnumField(RolePlayCommandGenEnum)
    formatter_man = fields.TextField()
    formatter_woman = fields.TextField()
    all_ending = fields.TextField()

    class Meta:
        table = "role_play"


class RolePlayCommandPydantic(BaseModel):
    name: str
    gen: RolePlayCommandGenEnum
    formatter_man: str
    formatter_woman: str
    all_ending: str

    @classmethod
    def load(cls: Type['RolePlayCommandPydantic'], model: RolePlayCommand) -> 'RolePlayCommandPydantic':
        return cls(
            name=model.name,
            gen=model.gen,
            formatter_man=model.formatter_man,
            formatter_woman=model.formatter_woman,
            all_ending=model.all_ending
        )

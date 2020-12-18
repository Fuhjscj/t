from enum import Enum

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

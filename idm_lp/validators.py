from typing import Optional

from asgiref.sync import async_to_sync
from tortoise.exceptions import DoesNotExist
from vbml import Patcher

from idm_lp.const import config
from idm_lp.models import Alias, RolePlayCommand, AliasPydantic, RolePlayCommandPydantic
from idm_lp.utils.temp import AliasTemp, RolePlayCommandTemp


def alias(value: str) -> Optional[AliasPydantic]:
    return AliasTemp.get_by_name(value.lower())


def role_play_command(value: str) -> Optional[RolePlayCommandPydantic]:
    return RolePlayCommandTemp.get_by_name(value.lower())


def prefix_self(value: str):
    if value.lower() in config['Prefixes']['self'].split(','):
        return value.lower()


def prefix_duty(value: str):
    if value.lower() in config['Prefixes']['duty'].split(','):
        return value.lower()


def prefix_service(value: str):
    if value.lower() in config['Prefixes']['service'].split(','):
        return value.lower()


patcher = Patcher.get_current()
setattr(patcher.validators, 'alias', alias)
setattr(patcher.validators, 'role_play_command', role_play_command)
setattr(patcher.validators, 'prefix_self', prefix_self)
setattr(patcher.validators, 'prefix_duty', prefix_duty)
setattr(patcher.validators, 'prefix_service', prefix_service)
Patcher.set_current(patcher)

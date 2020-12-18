from typing import Optional
from asgiref.sync import async_to_sync

from tortoise.exceptions import DoesNotExist
from vbml.blanket import validator

from idm_lp.const import config
from idm_lp.models import Alias, RolePlayCommand


@validator
@async_to_sync
async def alias(value: str) -> Optional[Alias]:
    try:
        return await Alias.get(name=value.lower())
    except DoesNotExist:
        return


@validator
@async_to_sync
async def role_play_command(value: str) -> Optional[RolePlayCommand]:
    try:
        return await RolePlayCommand.get(name=value.lower())
    except DoesNotExist:
        return


@validator
def prefix_self(value: str):
    return value.lower() in config['Prefixes']['self'].split(',')


@validator
def prefix_duty(value: str):
    return value.lower() in config['Prefixes']['duty'].split(',')


@validator
def prefix_service(value: str):
    return value.lower() in config['Prefixes']['service'].split(',')

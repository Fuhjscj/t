from typing import List, Optional

from idm_lp.models import Alias, AliasPydantic, RolePlayCommand, RolePlayCommandPydantic


class AliasTemp:
    data: List[AliasPydantic] = []

    @classmethod
    def get_by_name(cls, name: str) -> Optional[AliasPydantic]:
        for alias in cls.data:
            if alias.name == name:
                return alias

    @classmethod
    async def load_from_db(cls):
        cls.data = []
        async for alias in Alias.all():
            cls.data.append(AliasPydantic.load(alias))

    @classmethod
    async def create(cls, **kwargs):
        alias = await Alias.create(**kwargs)
        cls.data.append(AliasPydantic.load(alias))
        return alias


class RolePlayCommandTemp:
    data: List[RolePlayCommandPydantic] = []

    @classmethod
    def get_by_name(cls, name: str) -> Optional[RolePlayCommandPydantic]:
        for role_play_command in cls.data:
            if role_play_command.name == name:
                return role_play_command

    @classmethod
    async def load_from_db(cls):
        cls.data = []
        async for alias in RolePlayCommand.all():
            cls.data.append(RolePlayCommandPydantic.load(alias))

    @classmethod
    async def create(cls, **kwargs) -> RolePlayCommand:
        role_play_command = await RolePlayCommand.create(**kwargs)
        cls.data.append(RolePlayCommandPydantic.load(role_play_command))
        return role_play_command

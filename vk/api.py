import typing

from tools.dotdict import DotDict
from vk.errors.handlers import ErrorHandler
from vk.generators import ConsistentTokenGenerator
from vk.requests import Request

import aiohttp


class API:

    def __init__(
            self,
            tokens: typing.Union[str, typing.List[str]] = None,
            raise_errors: bool = True
    ):
        if not isinstance(tokens, list):
            tokens = [tokens]

        self.token_generator = ConsistentTokenGenerator(tokens)
        self.throw_errors = raise_errors
        self.session = aiohttp.ClientSession()

        self._user_id: typing.Optional[int] = None

    async def __call__(self, method, **kwargs):
        return await self.request(method, params=kwargs or {})

    async def request(self, method: str, params: dict, **kwargs) -> DotDict:
        for k, v in params.items():
            if isinstance(v, (tuple, list)):
                params[k] = ",".join(str(i) for i in v)

        _request = Request(
            self.session,
            self.token_generator,
            error_handlers=ErrorHandler.all(),
            version="5.103"
        )
        return await _request(method, params, **kwargs)

    @property
    async def user_id(self):
        if self._user_id:
            return self._user_id
        self._user_id = (await self.request('users.get', {}))[0].id

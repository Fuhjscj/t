from typing import List, Union, Type
import aiohttp

from tools.dotdict import DotDict
from vk.errors.handlers import ErrorHandler
from vk.generators import ConsistentTokenGenerator

import vk.errors.exceptions as errors


class Request:

    def __init__(
            self,
            session: aiohttp.ClientSession,
            tokens: ConsistentTokenGenerator,
            error_handlers: List[Type['ErrorHandler']],
            version: str = "5.103"
    ):
        self.session = session
        self.__tokens = tokens
        self.error_handlers = error_handlers
        self.version = version

    async def __call__(
            self,
            method,
            params,
            raise_errors: bool = None,
            raw_response: bool = False,
    ):
        response: aiohttp.ClientResponse
        url = "https://api.vk.com/method/{method}?access_token={token}&v={version}&lang=ru".format(
            method=method,
            token=await self.__tokens.get_token(),
            version=self.version
        )
        if not hasattr(self, 'session') or not self.session or self.session.closed:
            self.session = aiohttp.ClientSession()
        async with self.session.post(url, data=params) as response:
            if response.status == 200:
                raw_data = DotDict(await response.json())
                if raw_response:
                    return raw_data

                if 'error' in raw_data and raise_errors:
                    raise errors.VkApiException(
                        raw_data['error'],
                        self.__tokens,
                        method,
                        params
                    )
                else:
                    return raw_data.response
            else:
                raise errors.HttpException(response)

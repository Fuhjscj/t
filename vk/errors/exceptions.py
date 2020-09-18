import aiohttp

from tools.dotdict import DotDict
from vk.generators import ConsistentTokenGenerator


class ApiException(Exception):
    pass


class HttpException(ApiException):

    def __init__(
            self,
            response: aiohttp.ClientResponse
    ):
        self.response = response

    def __str__(self):
        return f"Invalid status code: %d" % self.response.status


class VkApiException(ApiException):

    def __init__(
            self,
            error_data: DotDict,
            tokens: ConsistentTokenGenerator,
            method: str,
            params: dict,
    ):
        self.error_data = error_data
        self.__tokens = tokens
        self.method = method
        self.params = params
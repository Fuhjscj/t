from abc import abstractmethod
from typing import Type, List

from vk.errors.exceptions import ApiException


class ErrorHandler:
    __all_handlers = []

    ERROR_CODE = 0

    def __init_subclass__(cls, **kwargs):
        super(ErrorHandler, cls).__init_subclass__(**kwargs)
        cls.__all_handlers.append(cls)

    def __init__(self, e: ApiException):
        self.exception = e

    @classmethod
    def all(cls) -> List[Type['ErrorHandler']]:
        return cls.__all_handlers

    @abstractmethod
    async def process(self):
        pass

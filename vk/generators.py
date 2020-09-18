# by https://github.com/timoniq/vkbottle

import typing
from abc import ABC, abstractmethod


class AbstractTokenGenerator(ABC):
    async def __aenter__(self, *args, **kwargs):
        return await self.get_token(*args, **kwargs)

    def __repr__(self):
        return f"<{self.__class__.__qualname__} tokens_amount={self.__len__()}>"

    def __len__(self):
        tokens: typing.Optional[typing.Iterable[str]] = getattr(self, "tokens")
        if tokens is None:
            tokens = []
        return len(tokens)

    @abstractmethod
    async def get_token(self, *args, **kwargs) -> str:
        pass


class ConsistentTokenGenerator(AbstractTokenGenerator):

    def __init__(self, tokens: typing.List[str]):
        self.tokens = tokens
        self.state = 0

    async def get_token(self, *args, **kwargs) -> str:
        index = self.state
        self.state = index + 1 if index + 1 < len(self.tokens) else 0
        return self.tokens[index]

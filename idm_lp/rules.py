from tortoise.exceptions import DoesNotExist
from vkbottle.framework.framework.rule import AbstractMessageRule, Message
from .models import IgnoredMember, IgnoredGlobalMember, MutedMember


class IgnoredMemberRule(AbstractMessageRule):

    async def check(self, message: Message) -> bool:
        try:
            await IgnoredMember.get(member_id=message.from_id, chat_id=message.peer_id)
            return True
        except DoesNotExist:
            return False


class IgnoredGlobalMemberRule(AbstractMessageRule):

    async def check(self, message: Message) -> bool:
        try:
            await IgnoredGlobalMember.get(member_id=message.from_id)
            return True
        except DoesNotExist:
            return False


class MutedMemberRule(AbstractMessageRule):
    async def check(self, message: Message) -> bool:
        try:
            await MutedMember.get(member_id=message.from_id, chat_id=message.peer_id)
            return True
        except DoesNotExist:
            return False

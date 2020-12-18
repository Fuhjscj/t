from tortoise import Model, fields


class IgnoredMember(Model):
    member_id = fields.IntField()
    chat_id = fields.IntField()

    class Meta:
        table = "ignored"
        unique_together = (('member_id', 'chat_id',),)


class MutedMember(IgnoredMember):

    class Meta:
        table = "muted"
        unique_together = (('member_id', 'chat_id',),)


class IgnoredGlobalMember(Model):
    member_id = fields.IntField(unique=True)

    class Meta:
        table = "global_ignored"

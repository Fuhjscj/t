from tortoise import Model, fields


class Alias(Model):
    name = fields.CharField(max_length=512, unique=True)
    command_from = fields.TextField()
    command_to = fields.TextField()

    class Meta:
        table = "aliases"

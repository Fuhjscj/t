from . import ping
from .signals import blueprints

blueprints = (
    ping.user,
    *blueprints,
)


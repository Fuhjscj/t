from . import info
from . import ping
from .signals import blueprints

blueprints = (
    info.user,
    ping.user,
    *blueprints,
)


from . import info
from . import ping

from .managers import blueprints as managers_blueprints
from .signals import blueprints as signals_blueprints


blueprints = (
    info.user,
    ping.user,
    *managers_blueprints,
    *signals_blueprints,
)


from typing import Callable, List

from .secret import create_secret
from .user import create_admin


commands: List[Callable[..., None]] = [create_secret, create_admin]

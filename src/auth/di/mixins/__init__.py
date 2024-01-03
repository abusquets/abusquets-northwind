from auth.di.mixins.token import TokenContainerMixin
from auth.di.mixins.user import UserContainerMixin


class AuthContainerMixin(UserContainerMixin, TokenContainerMixin):
    pass

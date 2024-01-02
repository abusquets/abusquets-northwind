from auth.adapters.spi.repositories.user import UserRepository
from auth.domain.ports.repositories.user import AbstractUserRepository
from infra.database.sqlalchemy.session import AbstractDatabase


class UserContainerMixin:
    db: AbstractDatabase
    user_repository: AbstractUserRepository

    def _get_user_repository(self) -> AbstractUserRepository:
        return UserRepository(self.db.session)

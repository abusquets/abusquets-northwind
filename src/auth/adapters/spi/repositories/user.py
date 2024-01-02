from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import registry

from auth.domain.entities.user import User
from auth.domain.ports.repositories.user import AbstractUserRepository, CreateUserInDTO, UpdatePartialUserInDTO
from auth.infra.database.sqlalchemy.models.user import users
from shared.exceptions import AlreadyExistsError
from shared.repository.sqlalchemy import SqlAlchemyRepository


mapper_registry = registry()


mapper_registry.map_imperatively(
    User,
    users,
)


class UserRepository(
    SqlAlchemyRepository[User, CreateUserInDTO, UpdatePartialUserInDTO],
    AbstractUserRepository,
):
    key = 'email'

    async def create(self, data: CreateUserInDTO) -> User:
        try:
            ret = await super().create(data)
        except IntegrityError as e:
            if 'duplicate key value violates unique constraint "uq_core_user_email"' in str(e):
                raise AlreadyExistsError(User.__name__)
        return ret

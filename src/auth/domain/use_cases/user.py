from auth.domain.entities.user import User
from auth.domain.services.user import CreateUserInDTO, UserService
from shared.exceptions import APPExceptionError
from shared.presenter import AbstractPresenter


class InvalidPasswordExceptionError(APPExceptionError):
    status_code = 401
    code = 'invalid-password'
    message = 'Invalid password'


class CreateUserUseCase:
    def __init__(self, presenter: AbstractPresenter, service: UserService):
        self.presenter = presenter
        self.service = service

    async def execute(self, in_dto: CreateUserInDTO) -> None:
        user = await self.service.create_user(in_dto)
        await self.presenter.present(user)


class GetUserAndVerifyPasswordUseCase:
    def __init__(self, presenter: AbstractPresenter, service: UserService):
        self.presenter = presenter
        self.service = service

    async def execute(self, username: str, password: str) -> None:
        user = await self.service.get_user_by_username(username)
        if not User.verify_password(password, user.password):
            raise InvalidPasswordExceptionError()

        await self.presenter.present(user)

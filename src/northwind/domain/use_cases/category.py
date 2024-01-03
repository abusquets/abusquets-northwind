from northwind.domain.services.category import Categorieservice
from northwind.schemas.category import CreateCategoryInDTO
from shared.api.schemas.page import PageParams
from shared.presenter import AbstractPresenter


class GetCategoriesUseCase:
    def __init__(self, presenter: AbstractPresenter, service: Categorieservice):
        self.presenter = presenter
        self.service = service

    async def execute(self, page_params: PageParams) -> None:
        await self.presenter.present(await self.service.get_categories(page_params=page_params))


class GetCategoryUseCase:
    def __init__(self, presenter: AbstractPresenter, service: Categorieservice):
        self.presenter = presenter
        self.service = service

    async def execute(self, id: int) -> None:
        await self.presenter.present(await self.service.get_category_by_id(id))


class CreateCategoryUseCase:
    def __init__(self, presenter: AbstractPresenter, service: Categorieservice):
        self.presenter = presenter
        self.service = service

    async def execute(self, in_dto: CreateCategoryInDTO) -> None:
        await self.presenter.present(await self.service.create_category(in_dto))


class UpdateCategoryUseCase:
    def __init__(self, presenter: AbstractPresenter, service: Categorieservice):
        self.presenter = presenter
        self.service = service

    async def execute(self, id: int, in_data: CreateCategoryInDTO) -> None:
        await self.presenter.present(await self.service.update_category(id, in_data))

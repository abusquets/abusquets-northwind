from northwind.domain.services.product import ProductService
from northwind.schemas.product import CreateProductInDTO
from shared.api.schemas.page import PageParams
from shared.presenter import AbstractPresenter


class GetProductsUseCase:
    def __init__(self, presenter: AbstractPresenter, service: ProductService):
        self.presenter = presenter
        self.service = service

    async def execute(self, page_params: PageParams) -> None:
        await self.presenter.present(await self.service.get_products(page_params=page_params))


class GetProductUseCase:
    def __init__(self, presenter: AbstractPresenter, service: ProductService):
        self.presenter = presenter
        self.service = service

    async def execute(self, id: int) -> None:
        await self.presenter.present(await self.service.get_product_by_id(id))


class CreateProductUseCase:
    def __init__(self, presenter: AbstractPresenter, service: ProductService):
        self.presenter = presenter
        self.service = service

    async def execute(self, in_dto: CreateProductInDTO) -> None:
        await self.presenter.present(await self.service.create_product(in_dto))


class UpdateProductUseCase:
    def __init__(self, presenter: AbstractPresenter, service: ProductService):
        self.presenter = presenter
        self.service = service

    async def execute(self, id: int, in_data: CreateProductInDTO) -> None:
        await self.presenter.present(await self.service.update_product(id, in_data))

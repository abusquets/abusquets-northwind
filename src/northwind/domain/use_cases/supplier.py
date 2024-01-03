from northwind.domain.services.supplier import SupplierService
from northwind.schemas.supplier import CreateSupplierInDTO
from shared.api.schemas.page import PageParams
from shared.presenter import AbstractPresenter


class GetSuppliersUseCase:
    def __init__(self, presenter: AbstractPresenter, service: SupplierService):
        self.presenter = presenter
        self.service = service

    async def execute(self, page_params: PageParams) -> None:
        await self.presenter.present(await self.service.get_suppliers(page_params=page_params))


class GetSupplierUseCase:
    def __init__(self, presenter: AbstractPresenter, service: SupplierService):
        self.presenter = presenter
        self.service = service

    async def execute(self, id: int) -> None:
        await self.presenter.present(await self.service.get_supplier_by_id(id))


class CreateSupplierUseCase:
    def __init__(self, presenter: AbstractPresenter, service: SupplierService):
        self.presenter = presenter
        self.service = service

    async def execute(self, in_dto: CreateSupplierInDTO) -> None:
        await self.presenter.present(await self.service.create_supplier(in_dto))


class UpdateSupplierUseCase:
    def __init__(self, presenter: AbstractPresenter, service: SupplierService):
        self.presenter = presenter
        self.service = service

    async def execute(self, id: int, in_data: CreateSupplierInDTO) -> None:
        await self.presenter.present(await self.service.update_supplier(id, in_data))

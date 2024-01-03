from typing import List, Optional

from northwind.domain.entities.supplier import Supplier
from northwind.domain.ports.repositories.supplier import AbstractSupplierRepository
from northwind.schemas.supplier import CreateSupplierInDTO, UpdateSupplierInDTO
from shared.api.schemas.page import PageParams


class SupplierService:
    def __init__(self, supplier_repository: AbstractSupplierRepository):
        self.supplier_repository = supplier_repository

    async def get_supplier_by_id(self, id: int) -> Supplier:
        return await self.supplier_repository.get_by_id(id)

    async def get_suppliers(self, *, page_params: Optional[PageParams] = None) -> List[Supplier]:
        if not page_params:
            ret = await self.supplier_repository.get_all()
        else:
            ret = await self.supplier_repository.get_xpage(page_params.page, page_params.size)
        return ret

    async def create_supplier(self, in_dto: CreateSupplierInDTO) -> Supplier:
        return await self.supplier_repository.create(in_dto)

    async def update_supplier(self, id: int, in_dto: UpdateSupplierInDTO) -> Supplier:
        return await self.supplier_repository.update(id, in_dto)

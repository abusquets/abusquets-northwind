from typing import List, Optional

from northwind.domain.entities.product import Product
from northwind.domain.ports.repositories.product import AbstractProductRepository
from northwind.schemas.product import CreateProductInDTO, UpdateProductInDTO
from shared.api.schemas.page import PageParams


class ProductService:
    def __init__(self, product_repository: AbstractProductRepository):
        self.product_repository = product_repository

    async def get_product_by_id(self, id: int) -> Product:
        return await self.product_repository.get_by_id(id)

    async def get_products(self, *, page_params: Optional[PageParams] = None) -> List[Product]:
        if not page_params:
            ret = await self.product_repository.get_all()
        else:
            ret = await self.product_repository.get_xpage(page_params.page, page_params.size)
        return ret

    async def create_product(self, in_dto: CreateProductInDTO) -> Product:
        return await self.product_repository.create(in_dto)

    async def update_product(self, id: int, in_dto: UpdateProductInDTO) -> Product:
        return await self.product_repository.update(id, in_dto)

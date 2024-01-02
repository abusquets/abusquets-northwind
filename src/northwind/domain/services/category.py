from typing import List, Optional

from northwind.domain.entities.category import Category
from northwind.domain.ports.repositories.category import AbstractCategoryRepository
from northwind.schemas.category import CreateCategoryInDTO, UpdateCategoryInDTO
from shared.api.schemas.page import PageParams


class Categorieservice:
    def __init__(self, category_repository: AbstractCategoryRepository):
        self.category_repository = category_repository

    async def get_category_by_id(self, id: int) -> Category:
        return await self.category_repository.get_by_id(id)

    async def get_categories(self, *, page_params: Optional[PageParams] = None) -> List[Category]:
        if not page_params:
            ret = await self.category_repository.get_all()
        else:
            ret = await self.category_repository.get_xpage(page_params.page, page_params.size)
        return ret

    async def create_category(self, in_dto: CreateCategoryInDTO) -> Category:
        return await self.category_repository.create(in_dto)

    async def update_category(self, id: int, in_dto: UpdateCategoryInDTO) -> Category:
        return await self.category_repository.update(id, in_dto)

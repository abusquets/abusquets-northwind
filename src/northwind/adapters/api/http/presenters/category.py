from typing import List

from northwind.adapters.api.http.schemas.category import CategoryListPagedResponse, CategoryResponse
from northwind.domain.entities.category import Category
from shared.api.schemas.page import PageParams
from shared.presenter import AbstractPresenter


class CategoryPresenter(AbstractPresenter[Category, CategoryResponse]):
    result: CategoryResponse

    async def present(self, data: Category) -> None:
        self.result = CategoryResponse.model_validate(data, from_attributes=True)


class CategoryPagedListPresenter(AbstractPresenter[List[Category], List[CategoryResponse]]):
    result: CategoryListPagedResponse

    def __init__(self, page_params: PageParams) -> None:
        self.page_params = page_params

    async def present(self, data: List[Category]) -> None:
        list_items = [CategoryResponse.model_validate(item, from_attributes=True) for item in data]
        self.result = CategoryListPagedResponse(
            results=list_items,
            total=len(list_items),
            page=self.page_params.page,
            size=self.page_params.size,
        )

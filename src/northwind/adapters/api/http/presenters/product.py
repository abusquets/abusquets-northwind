from typing import List

from northwind.adapters.api.http.schemas.product import ProductListPagedResponse, ProductResponse
from northwind.domain.entities.product import Product
from shared.api.schemas.page import PageParams
from shared.presenter import AbstractPresenter


class ProductPresenter(AbstractPresenter[Product, ProductResponse]):
    result: ProductResponse

    async def present(self, data: Product) -> None:
        self.result = ProductResponse.model_validate(data, from_attributes=True)


class ProductPagedListPresenter(AbstractPresenter[List[Product], List[ProductResponse]]):
    result: ProductListPagedResponse

    def __init__(self, page_params: PageParams) -> None:
        self.page_params = page_params

    async def present(self, data: List[Product]) -> None:
        list_items = [ProductResponse.model_validate(item, from_attributes=True) for item in data]
        self.result = ProductListPagedResponse(
            results=list_items,
            total=len(list_items),
            page=self.page_params.page,
            size=self.page_params.size,
        )

from typing import List

from northwind.adapters.api.http.schemas.supplier import SupplierListPagedResponse, SupplierResponse
from northwind.domain.entities.supplier import Supplier
from shared.api.schemas.page import PageParams
from shared.presenter import AbstractPresenter


class SupplierPresenter(AbstractPresenter[Supplier, SupplierResponse]):
    result: SupplierResponse

    async def present(self, data: Supplier) -> None:
        self.result = SupplierResponse.model_validate(data, from_attributes=True)


class SupplierPagedListPresenter(AbstractPresenter[List[Supplier], List[SupplierResponse]]):
    result: SupplierListPagedResponse

    def __init__(self, page_params: PageParams) -> None:
        self.page_params = page_params

    async def present(self, data: List[Supplier]) -> None:
        list_items = [SupplierResponse.model_validate(item, from_attributes=True) for item in data]
        self.result = SupplierListPagedResponse(
            results=list_items,
            total=len(list_items),
            page=self.page_params.page,
            size=self.page_params.size,
        )

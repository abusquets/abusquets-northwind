from typing import Optional

from pydantic import BaseModel, ConfigDict

from northwind.schemas.product import CreateProductInDTO, UpdatePartialProductInDTO, UpdateProductInDTO
from shared.api.schemas.page import PagedResponseSchema


class Supplier(BaseModel):
    id: int
    company_name: str


class Category(BaseModel):
    id: int
    name: str


class ProductResponse(BaseModel):
    id: int
    name: str
    supplier: Supplier
    category: Category
    quantity_per_unit: str
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int
    discontinued: Optional[int] = None


class ProductListPagedResponse(PagedResponseSchema[ProductResponse]):
    pass


class CreateProductRequestDTO(CreateProductInDTO):
    model_config = ConfigDict(extra='ignore')


class CreateProductResponseDTO(ProductResponse):
    pass


class UpdateProductRequestDTO(UpdateProductInDTO):
    model_config = ConfigDict(extra='ignore')


class UpdatePartialProductRequestDTO(UpdatePartialProductInDTO):
    model_config = ConfigDict(extra='ignore')

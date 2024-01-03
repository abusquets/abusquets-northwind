from typing import Optional

from pydantic import BaseModel, Field


class CreateProductInDTO(BaseModel):
    name: str = Field(min_length=1, max_length=40)
    supplier_id: int
    category_id: int
    quantity_per_unit: str = Field(max_length=20)
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int
    discontinued: Optional[int] = None


class UpdateProductInDTO(CreateProductInDTO):
    pass


class UpdatePartialProductInDTO(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=40)
    supplier_id: Optional[int] = None
    category_id: Optional[int] = None
    quantity_per_unit: str = Field(default=None, max_length=20)
    unit_price: Optional[float] = None
    units_in_stock: Optional[int] = None
    units_on_order: Optional[int] = None
    reorder_level: Optional[int] = None
    discontinued: Optional[int] = None

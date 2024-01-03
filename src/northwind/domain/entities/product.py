from dataclasses import dataclass
from typing import Optional

from northwind.domain.entities.category import Category
from northwind.domain.entities.supplier import Supplier
from northwind.domain.entities.value_objects import ProductId


@dataclass(kw_only=True)
class Product:
    id: Optional[ProductId] = None
    name: str
    supplier: Supplier
    category: Category
    quantity_per_unit: str
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int
    discontinued: Optional[int] = None

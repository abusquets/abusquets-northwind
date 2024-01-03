from dataclasses import dataclass
from typing import Optional

from northwind.domain.entities.value_objects import CategoryId


@dataclass(kw_only=True)
class Category:
    id: Optional[CategoryId] = None
    name: str
    description: Optional[str] = None

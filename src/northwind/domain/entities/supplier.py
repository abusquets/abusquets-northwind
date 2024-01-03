from dataclasses import dataclass
from typing import Optional

from northwind.domain.entities.value_objects import SupplierId


@dataclass(kw_only=True)
class Supplier:
    id: Optional[SupplierId] = None
    company_name: str
    contact_name: Optional[str] = None
    contact_title: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    homepage: Optional[str] = None

from typing import Optional

from pydantic import BaseModel, ConfigDict

from northwind.schemas.supplier import CreateSupplierInDTO, UpdatePartialSupplierInDTO, UpdateSupplierInDTO
from shared.api.schemas.page import PagedResponseSchema


class SupplierResponse(BaseModel):
    id: int
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


class SupplierListPagedResponse(PagedResponseSchema[SupplierResponse]):
    pass


class CreateSupplierRequestDTO(CreateSupplierInDTO):
    model_config = ConfigDict(extra='ignore')


class CreateSupplierResponseDTO(SupplierResponse):
    pass


class UpdateSupplierRequestDTO(UpdateSupplierInDTO):
    model_config = ConfigDict(extra='ignore')


class UpdatePartialSupplierRequestDTO(UpdatePartialSupplierInDTO):
    model_config = ConfigDict(extra='ignore')

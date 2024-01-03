from typing import Optional

from pydantic import BaseModel, Field


class CreateSupplierInDTO(BaseModel):
    name: str = Field(min_length=1, max_length=15)
    company_name: Optional[str] = Field(default=None, max_length=40)
    contact_name: Optional[str] = Field(default=None, max_length=30)
    contact_title: Optional[str] = Field(default=None, max_length=30)
    address: Optional[str] = Field(default=None, max_length=60)
    city: Optional[str] = Field(default=None, max_length=15)
    region: Optional[str] = Field(default=None, max_length=15)
    postal_code: Optional[str] = Field(default=None, max_length=10)
    country: Optional[str] = Field(default=None, max_length=15)
    phone: Optional[str] = Field(default=None, max_length=24)
    fax: Optional[str] = Field(default=None, max_length=24)
    homepage: Optional[str] = Field(default=None, max_length=1024)


class UpdateSupplierInDTO(CreateSupplierInDTO):
    pass


class UpdatePartialSupplierInDTO(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=15)
    company_name: Optional[str] = Field(default=None, max_length=40)
    contact_name: Optional[str] = Field(default=None, max_length=30)
    contact_title: Optional[str] = Field(default=None, max_length=30)
    address: Optional[str] = Field(default=None, max_length=60)
    city: Optional[str] = Field(default=None, max_length=15)
    region: Optional[str] = Field(default=None, max_length=15)
    postal_code: Optional[str] = Field(default=None, max_length=10)
    country: Optional[str] = Field(default=None, max_length=15)
    phone: Optional[str] = Field(default=None, max_length=24)
    fax: Optional[str] = Field(default=None, max_length=24)
    homepage: Optional[str] = Field(default=None, max_length=1024)

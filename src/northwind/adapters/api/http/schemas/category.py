from typing import Optional

from pydantic import BaseModel, ConfigDict

from northwind.schemas.category import CreateCategoryInDTO, UpdateCategoryInDTO, UpdatePartialCategoryInDTO
from shared.api.schemas.page import PagedResponseSchema


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class CategoryListPagedResponse(PagedResponseSchema[CategoryResponse]):
    pass


class CreateCategoryRequestDTO(CreateCategoryInDTO):
    model_config = ConfigDict(extra='ignore')


class CreateCategoryResponseDTO(CategoryResponse):
    pass


class UpdateCategoryRequestDTO(UpdateCategoryInDTO):
    model_config = ConfigDict(extra='ignore')


class UpdatePartialCategoryRequestDTO(UpdatePartialCategoryInDTO):
    model_config = ConfigDict(extra='ignore')

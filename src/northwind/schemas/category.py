from typing import Optional

from pydantic import BaseModel, Field


class CreateCategoryInDTO(BaseModel):
    name: str = Field(min_length=1, max_length=15)
    description: Optional[str] = Field(default=None, max_length=1024)


class UpdateCategoryInDTO(CreateCategoryInDTO):
    pass


class UpdatePartialCategoryInDTO(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=15)
    description: Optional[str] = Field(default=None, max_length=1024)

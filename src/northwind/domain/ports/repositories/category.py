from northwind.domain.entities.category import Category
from northwind.schemas.category import CreateCategoryInDTO, UpdatePartialCategoryInDTO
from shared.repository.ports.generic import AbstractRepository


class AbstractCategoryRepository(AbstractRepository[Category, CreateCategoryInDTO, UpdatePartialCategoryInDTO]):
    key = 'id'

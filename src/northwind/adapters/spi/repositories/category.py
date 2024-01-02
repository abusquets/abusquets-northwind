from sqlalchemy.orm import registry

from northwind.domain.entities.category import Category
from northwind.domain.ports.repositories.category import AbstractCategoryRepository
from northwind.infra.database.sqlalchemy.models import categories
from northwind.schemas.category import CreateCategoryInDTO, UpdatePartialCategoryInDTO
from shared.repository.sqlalchemy import SqlAlchemyRepository


mapper_registry = registry()
mapper_registry.map_imperatively(
    Category,
    categories,
    properties={
        'id': categories.c.category_id,
        'name': categories.c.category_name,
        'description': categories.c.description,
    },
)


class CategoryRepository(
    SqlAlchemyRepository[Category, CreateCategoryInDTO, UpdatePartialCategoryInDTO],
    AbstractCategoryRepository,
):
    pass

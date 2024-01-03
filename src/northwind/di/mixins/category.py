from infra.database.sqlalchemy.session import AbstractDatabase
from northwind.adapters.spi.repositories.category import CategoryRepository
from northwind.domain.ports.repositories.category import AbstractCategoryRepository


class CategoryContainerMixin:
    db: AbstractDatabase
    category_repository: AbstractCategoryRepository

    def _get_category_repository(self) -> AbstractCategoryRepository:
        return CategoryRepository(self.db.session)

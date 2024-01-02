from infra.database.sqlalchemy.session import AbstractDatabase
from northwind.adapters.spi.repositories.product import ProductRepository
from northwind.domain.ports.repositories.category import AbstractCategoryRepository
from northwind.domain.ports.repositories.product import AbstractProductRepository
from northwind.domain.ports.repositories.supplier import AbstractSupplierRepository


class ProductContainerMixin:
    db: AbstractDatabase
    product_repository: AbstractProductRepository
    category_repository: AbstractCategoryRepository
    supplier_repository: AbstractSupplierRepository

    def _get_product_repository(self) -> AbstractProductRepository:
        return ProductRepository(self.db.session, self.category_repository, self.supplier_repository)

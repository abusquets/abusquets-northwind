from infra.database.sqlalchemy.session import AbstractDatabase
from northwind.adapters.spi.repositories.supplier import SupplierRepository
from northwind.domain.ports.repositories.supplier import AbstractSupplierRepository


class SupplierContainerMixin:
    db: AbstractDatabase
    supplier_repository: AbstractSupplierRepository

    def _get_supplier_repository(self) -> AbstractSupplierRepository:
        return SupplierRepository(self.db.session)

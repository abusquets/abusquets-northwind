from sqlalchemy.orm import registry

from northwind.domain.entities.supplier import Supplier
from northwind.domain.ports.repositories.supplier import AbstractSupplierRepository
from northwind.infra.database.sqlalchemy.models import suppliers
from northwind.schemas.supplier import CreateSupplierInDTO, UpdatePartialSupplierInDTO
from shared.repository.sqlalchemy import SqlAlchemyRepository


mapper_registry = registry()
mapper_registry.map_imperatively(
    Supplier,
    suppliers,
    properties={'id': suppliers.c.supplier_id},
)


class SupplierRepository(
    SqlAlchemyRepository[Supplier, CreateSupplierInDTO, UpdatePartialSupplierInDTO],
    AbstractSupplierRepository,
):
    pass

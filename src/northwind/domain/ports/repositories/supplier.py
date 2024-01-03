from northwind.domain.entities.supplier import Supplier
from northwind.schemas.supplier import CreateSupplierInDTO, UpdatePartialSupplierInDTO
from shared.repository.ports.generic import AbstractRepository


class AbstractSupplierRepository(AbstractRepository[Supplier, CreateSupplierInDTO, UpdatePartialSupplierInDTO]):
    key = 'id'

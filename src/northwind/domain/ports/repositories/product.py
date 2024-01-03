from northwind.domain.entities.product import Product
from northwind.schemas.product import CreateProductInDTO, UpdatePartialProductInDTO
from shared.repository.ports.generic import AbstractRepository


class AbstractProductRepository(AbstractRepository[Product, CreateProductInDTO, UpdatePartialProductInDTO]):
    key = 'id'

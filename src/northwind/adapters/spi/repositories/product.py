from typing import AsyncContextManager, Callable, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import registry, relationship

from northwind.domain.entities.category import Category
from northwind.domain.entities.product import Product
from northwind.domain.entities.supplier import Supplier
from northwind.domain.ports.repositories.category import AbstractCategoryRepository
from northwind.domain.ports.repositories.product import AbstractProductRepository
from northwind.domain.ports.repositories.supplier import AbstractSupplierRepository
from northwind.infra.database.sqlalchemy.models import products
from northwind.schemas.product import CreateProductInDTO, UpdatePartialProductInDTO
from shared.repository.sqlalchemy import SqlAlchemyRepository


mapper_registry = registry()
mapper_registry.map_imperatively(
    Product,
    products,
    properties={
        'id': products.c.product_id,
        'name': products.c.product_name,
        'category': relationship(Category, lazy='joined'),
        'supplier': relationship(Supplier, lazy='joined'),
    },
)

AsyncSessionCtxT = Callable[[], AsyncContextManager[AsyncSession]]


class ProductRepository(
    SqlAlchemyRepository[Product, CreateProductInDTO, UpdatePartialProductInDTO],
    AbstractProductRepository,
):
    def __init__(
        self,
        session: AsyncSessionCtxT,
        category_repository: AbstractCategoryRepository,
        supplier_repository: AbstractSupplierRepository,
    ) -> None:
        super().__init__(session)
        self.category_repository = category_repository
        self.supplier_repository = supplier_repository

    async def create(self, data: CreateProductInDTO) -> Product:
        async with self.session_factory() as session:
            in_data = data.model_dump(exclude={'category_id', 'supplier_id'})
            category = await self.category_repository.get_by_id(data.category_id)
            supplier = await self.supplier_repository.get_by_id(data.supplier_id)
            instance = self.entity(**in_data, category=category, supplier=supplier)
            session.add(instance)
        return await self.get_by_id(instance.id or -1)

    async def update(self, uuid: Union[str, int], data: UpdatePartialProductInDTO) -> Product:
        object_id = int(uuid) if isinstance(uuid, str) else uuid
        to_update = data.model_dump(exclude_unset=True)
        if not to_update:
            raise ValueError('No data to update')

        async with self.session_factory() as session:
            instance = await self.get_by_id(object_id)

            for key, value in to_update.items():
                if key == 'category_id' and value != instance.category.id:
                    category = await self.category_repository.get_by_id(value)
                    instance.category = category
                    continue
                if key == 'supplier_id' and value != instance.supplier.id:
                    supplier = await self.supplier_repository.get_by_id(value)
                    instance.supplier = supplier
                    continue

                setattr(instance, key, value)

            session.add(instance)

        return await self.get_by_id(object_id)

from typing import AsyncContextManager, AsyncGenerator, Callable, Dict, Optional, Union

from faker import Faker
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from northwind.infra.database.sqlalchemy.models import categories


fake = Faker()

AsyncSessionCtxT = Callable[[], AsyncContextManager[AsyncSession]]


@pytest_asyncio.fixture
async def category_factory(
    async_session_maker: AsyncSessionCtxT,
) -> Callable[[str], AsyncGenerator[dict[str, str | int], None]]:
    async def _create_category(
        name: str, description: Optional[str] = None
    ) -> AsyncGenerator[Dict[str, Union[str, int]], None]:
        async with async_session_maker() as session:
            description = description or fake.paragraph(nb_sentences=2)
            statement = (
                categories.insert()
                .values(category_name=name, description=description)
                .returning(categories.c.category_id)
            )
            result = await session.execute(statement)
            await session.commit()

            object_id = result.scalar_one()

            yield {'id': object_id, 'name': name, 'description': description}

            stmt = categories.delete().where(categories.c.category_id == object_id)
            await session.execute(stmt)

            await session.commit()

    return _create_category


@pytest_asyncio.fixture
async def category_cereals(
    category_factory: Callable[[str], AsyncGenerator[dict[str, str | int], None]],
) -> AsyncGenerator[Dict[str, Union[str, int]], None]:
    async for category in category_factory('Cereals'):
        yield category

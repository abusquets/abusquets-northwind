from typing import Callable, Dict, Union

import faker
from httpx import AsyncClient
import pytest


faker = faker.Faker()


@pytest.mark.asyncio
async def test_category_create(async_admin_client: AsyncClient) -> None:
    data = {'name': 'Fish', 'description': 'Fish Description'}
    response = await async_admin_client.post('/northwind/category', json=data)
    assert response.status_code == 201
    result = response.json()
    assert 'name' in result and result['name'] == data['name']
    assert 'description' in result and result['description'] == data['description']


@pytest.mark.asyncio
async def test_category_list(async_normal_client: AsyncClient, category_cereals: Dict[str, Union[str, int]]) -> None:
    response = await async_normal_client.get('/northwind/category')
    assert response.status_code == 200
    paginated_result = response.json()
    assert 'results' in paginated_result
    names = [item.get('name') for item in paginated_result['results']]
    assert category_cereals['name'] in names


@pytest.mark.asyncio
async def test_category_detail(async_normal_client: AsyncClient, category_cereals: Dict[str, Union[str, int]]) -> None:
    response = await async_normal_client.get(f'/northwind/category/{category_cereals.get("id")}')
    assert response.status_code == 200
    result = response.json()
    assert 'name' in result and result['name'] == category_cereals['name']
    assert 'description' in result and result['description'] == category_cereals['description']


@pytest.mark.asyncio
async def test_category_update(async_admin_client: AsyncClient, category_factory: Callable) -> None:
    async for category in category_factory(name=faker.pystr(max_chars=14)):
        data = {'name': 'Vegetables', 'description': 'Vegetables Description'}

        assert category['name'] != 'Vegetables'
        assert category['description'] != 'Vegetables Description'

        response = await async_admin_client.put(f'/northwind/category/{category["id"]}', json=data)
        assert response.status_code == 200
        result = response.json()
        assert 'name' in result
        assert result['name'] == 'Vegetables'
        assert 'description' in result
        assert result['description'] == 'Vegetables Description'


async def test_category_update_partial(async_admin_client: AsyncClient, category_factory: Callable) -> None:
    async for category in category_factory(name=faker.pystr(max_chars=14)):
        data = {'description': 'Vegetables'}
        assert category['description'] != data['description']
        response = await async_admin_client.patch(f'/northwind/category/{category["id"]}', json=data)
        assert response.status_code == 200
        result = response.json()
        assert 'description' in result
        assert result['description'] == data['description']

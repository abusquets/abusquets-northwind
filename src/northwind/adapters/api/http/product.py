from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app.app_container import AppContainer
from app.exceptions import EmptyPayloadExceptionError
from app.schemas import Session
from app.session_deps import is_admin_session
from northwind.adapters.api.http.presenters.product import (
    ProductPagedListPresenter,
    ProductPresenter,
)
from northwind.adapters.api.http.schemas.product import (
    CreateProductRequestDTO,
    CreateProductResponseDTO,
    ProductListPagedResponse,
    ProductResponse,
    UpdatePartialProductRequestDTO,
    UpdateProductRequestDTO,
)
from northwind.domain.entities.product import Product
from northwind.domain.services.product import ProductService
from northwind.domain.use_cases.product import (
    CreateProductUseCase,
    GetProductsUseCase,
    GetProductUseCase,
    UpdateProductUseCase,
)
from northwind.schemas.product import CreateProductInDTO, UpdatePartialProductInDTO
from shared.api.schemas.page import PageParams


router = APIRouter(prefix='/product')


@router.get(
    '/{uuid}',
    responses={
        200: {'description': 'Successful Response'},
        404: {'description': 'Product not found'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def get_product(
    id: int,
    container: AppContainer = Depends(AppContainer),
) -> ProductResponse:
    service = ProductService(container.product_repository)
    presenter = ProductPresenter()
    usecase = GetProductUseCase(presenter, service)
    await usecase.execute(id)
    return presenter.result


@router.get(
    '',
    responses={
        200: {'description': 'Successful Response'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def list_products(
    page_params: PageParams = Depends(),
    container: AppContainer = Depends(AppContainer),
) -> ProductListPagedResponse:
    service = ProductService(container.product_repository)
    presenter = ProductPagedListPresenter(page_params)
    usecase = GetProductsUseCase(presenter, service)
    await usecase.execute(page_params)
    return presenter.result


@router.post(
    '',
    response_class=JSONResponse,
    response_model=CreateProductResponseDTO,
    status_code=201,
    responses={
        201: {'description': 'Item created'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def create_product(
    request_data: CreateProductRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> Product:
    in_dto = CreateProductInDTO.model_validate(request_data.model_dump())
    service = ProductService(container.product_repository)
    presenter = ProductPresenter()
    usecase = CreateProductUseCase(presenter, service)
    await usecase.execute(in_dto)
    return presenter.result


@router.put(
    '/{id}',
    responses={
        200: {'description': 'Item updated'},
        404: {'description': 'Item not found'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def update_product(
    id: int,
    request_data: UpdateProductRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> ProductResponse:
    in_data = request_data.model_dump()
    in_dto = UpdatePartialProductInDTO.model_validate(in_data)
    service = ProductService(container.product_repository)
    presenter = ProductPresenter()
    usecase = UpdateProductUseCase(presenter, service)
    await usecase.execute(id, in_dto)
    return presenter.result


@router.patch(
    '/{id}',
    responses={
        200: {'description': 'Item updated'},
        404: {'description': 'Item not found'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def update_product_partially(
    id: int,
    request_data: UpdatePartialProductRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> ProductResponse:
    in_data = request_data.model_dump(exclude_unset=True)
    if not in_data.keys():
        raise EmptyPayloadExceptionError()
    in_dto = UpdatePartialProductInDTO.model_validate(in_data)

    service = ProductService(container.product_repository)
    presenter = ProductPresenter()
    usecase = UpdateProductUseCase(presenter, service)
    await usecase.execute(id, in_dto)
    return presenter.result

from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app.app_container import AppContainer
from app.exceptions import EmptyPayloadExceptionError
from app.schemas import Session
from app.session_deps import check_access_token, is_admin_session
from northwind.adapters.api.http.presenters.category import CategoryPagedListPresenter, CategoryPresenter
from northwind.adapters.api.http.schemas.category import (
    CategoryListPagedResponse,
    CategoryResponse,
    CreateCategoryRequestDTO,
    CreateCategoryResponseDTO,
    UpdateCategoryRequestDTO,
    UpdatePartialCategoryRequestDTO,
)
from northwind.domain.entities.category import Category
from northwind.domain.services.category import Categorieservice
from northwind.domain.use_cases.category import (
    CreateCategoryUseCase,
    GetCategoriesUseCase,
    GetCategoryUseCase,
    UpdateCategoryUseCase,
)
from northwind.schemas.category import CreateCategoryInDTO, UpdatePartialCategoryInDTO
from shared.api.schemas.page import PageParams


router = APIRouter(prefix='/category')


@router.get(
    '/{id}',
    responses={
        200: {'description': 'Successful Response'},
        404: {'description': 'Category not found'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def get_category(
    id: int,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(check_access_token),
) -> CategoryResponse:
    service = Categorieservice(container.category_repository)
    presenter = CategoryPresenter()
    usecase = GetCategoryUseCase(presenter, service)
    await usecase.execute(id)
    return presenter.result


@router.get(
    '',
    responses={
        200: {'description': 'Successful Response'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def list_categories(
    page_params: PageParams = Depends(),
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(check_access_token),
) -> CategoryListPagedResponse:
    service = Categorieservice(container.category_repository)
    presenter = CategoryPagedListPresenter(page_params)
    usecase = GetCategoriesUseCase(presenter, service)
    await usecase.execute(page_params)
    return presenter.result


@router.post(
    '',
    response_class=JSONResponse,
    response_model=CreateCategoryResponseDTO,
    status_code=201,
    responses={
        201: {'description': 'Item created'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def create_category(
    request_data: CreateCategoryRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> Category:
    in_dto = CreateCategoryInDTO.model_validate(request_data.model_dump())
    service = Categorieservice(container.category_repository)
    presenter = CategoryPresenter()
    usecase = CreateCategoryUseCase(presenter, service)
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
async def update_category(
    id: int,
    request_data: UpdateCategoryRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> CategoryResponse:
    in_data = request_data.model_dump()
    in_dto = UpdatePartialCategoryInDTO.model_validate(in_data)
    service = Categorieservice(container.category_repository)
    presenter = CategoryPresenter()
    usecase = UpdateCategoryUseCase(presenter, service)
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
async def update_category_partially(
    id: int,
    request_data: UpdatePartialCategoryRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> CategoryResponse:
    in_data = request_data.model_dump(exclude_unset=True)
    if not in_data.keys():
        raise EmptyPayloadExceptionError()
    in_dto = UpdatePartialCategoryInDTO.model_validate(in_data)

    service = Categorieservice(container.category_repository)
    presenter = CategoryPresenter()
    usecase = UpdateCategoryUseCase(presenter, service)
    await usecase.execute(id, in_dto)
    return presenter.result

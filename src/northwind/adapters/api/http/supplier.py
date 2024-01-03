from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app.app_container import AppContainer
from app.exceptions import EmptyPayloadExceptionError
from app.schemas import Session
from app.session_deps import check_access_token, is_admin_session
from northwind.adapters.api.http.presenters.supplier import SupplierPagedListPresenter, SupplierPresenter
from northwind.adapters.api.http.schemas.supplier import (
    CreateSupplierRequestDTO,
    CreateSupplierResponseDTO,
    SupplierListPagedResponse,
    SupplierResponse,
    UpdatePartialSupplierRequestDTO,
    UpdateSupplierRequestDTO,
)
from northwind.domain.entities.supplier import Supplier
from northwind.domain.services.supplier import SupplierService
from northwind.domain.use_cases.supplier import (
    CreateSupplierUseCase,
    GetSuppliersUseCase,
    GetSupplierUseCase,
    UpdateSupplierUseCase,
)
from northwind.schemas.supplier import CreateSupplierInDTO, UpdatePartialSupplierInDTO
from shared.api.schemas.page import PageParams


router = APIRouter(prefix='/supplier')


@router.get(
    '/{id}',
    responses={
        200: {'description': 'Successful Response'},
        404: {'description': 'Supplier not found'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def get_supplier(
    id: int,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(check_access_token),
) -> SupplierResponse:
    service = SupplierService(container.supplier_repository)
    presenter = SupplierPresenter()
    usecase = GetSupplierUseCase(presenter, service)
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
) -> SupplierListPagedResponse:
    service = SupplierService(container.supplier_repository)
    presenter = SupplierPagedListPresenter(page_params)
    usecase = GetSuppliersUseCase(presenter, service)
    await usecase.execute(page_params)
    return presenter.result


@router.post(
    '',
    response_class=JSONResponse,
    response_model=CreateSupplierResponseDTO,
    status_code=201,
    responses={
        201: {'description': 'Item created'},
        422: {'description': 'Unprocessable Entity'},
    },
)
async def create_supplier(
    request_data: CreateSupplierRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> Supplier:
    in_dto = CreateSupplierInDTO.model_validate(request_data.model_dump())
    service = SupplierService(container.supplier_repository)
    presenter = SupplierPresenter()
    usecase = CreateSupplierUseCase(presenter, service)
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
async def update_supplier(
    id: int,
    request_data: UpdateSupplierRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> SupplierResponse:
    in_data = request_data.model_dump()
    in_dto = UpdatePartialSupplierInDTO.model_validate(in_data)
    service = SupplierService(container.supplier_repository)
    presenter = SupplierPresenter()
    usecase = UpdateSupplierUseCase(presenter, service)
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
async def update_supplier_partially(
    id: int,
    request_data: UpdatePartialSupplierRequestDTO,
    container: AppContainer = Depends(AppContainer),
    _: Session = Depends(is_admin_session),
) -> SupplierResponse:
    in_data = request_data.model_dump(exclude_unset=True)
    if not in_data.keys():
        raise EmptyPayloadExceptionError()
    in_dto = UpdatePartialSupplierInDTO.model_validate(in_data)

    service = SupplierService(container.supplier_repository)
    presenter = SupplierPresenter()
    usecase = UpdateSupplierUseCase(presenter, service)
    await usecase.execute(id, in_dto)
    return presenter.result

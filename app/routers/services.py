from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse


router = APIRouter(
    prefix="/api/services",
    tags=["Services"]
)


@router.post(
    "/",
    response_model=ServiceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_service(
    service: ServiceCreate,
    db: Session = Depends(get_db)
):
    new_service = Service(
        name=service.name,
        description=service.description,
        price=service.price,
        duration=service.duration
    )

    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


@router.get(
    "/",
    response_model=list[ServiceResponse]
)
def list_services(
    db: Session = Depends(get_db)
):
    return db.query(Service).all()


@router.get(
    "/{service_id}",
    response_model=ServiceResponse
)
def get_service(
    service_id: int,
    db: Session = Depends(get_db)
):
    service = (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )

    if not service:
        raise HTTPException(
            status_code=404,
            detail="Serviço não encontrado."
        )

    return service


@router.put(
    "/{service_id}",
    response_model=ServiceResponse
)
def update_service(
    service_id: int,
    service_data: ServiceUpdate,
    db: Session = Depends(get_db)
):
    service = (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )

    if not service:
        raise HTTPException(
            status_code=404,
            detail="Serviço não encontrado."
        )

    if service_data.name is not None:
        service.name = service_data.name

    if service_data.description is not None:
        service.description = service_data.description

    if service_data.price is not None:
        service.price = service_data.price

    if service_data.duration is not None:
        service.duration = service_data.duration

    db.commit()
    db.refresh(service)

    return service


@router.delete(
    "/{service_id}",
    response_model=ServiceResponse
)
def delete_service(
    service_id: int,
    db: Session = Depends(get_db)
):
    service = (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )

    if not service:
        raise HTTPException(
            status_code=404,
            detail="Serviço não encontrado."
        )

    db.delete(service)
    db.commit()

    return service
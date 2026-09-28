from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceResponse


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
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.manicure import Manicure
from app.schemas.manicure import ManicureCreate, ManicureUpdate, ManicureResponse


router = APIRouter(
    prefix="/api/manicures",
    tags=["Manicures"]
)


@router.post(
    "/",
    response_model=ManicureResponse,
    status_code=status.HTTP_201_CREATED
)
def create_manicure(
    manicure: ManicureCreate,
    db: Session = Depends(get_db)
):
    new_manicure = Manicure(
        name=manicure.name,
        phone=manicure.phone,
        active=True
    )

    db.add(new_manicure)
    db.commit()
    db.refresh(new_manicure)

    return new_manicure


@router.get(
    "/",
    response_model=list[ManicureResponse]
)
def list_manicures(
    db: Session = Depends(get_db)
):
    return db.query(Manicure).all()


@router.get(
    "/{manicure_id}",
    response_model=ManicureResponse
)
def get_manicure(
    manicure_id: int,
    db: Session = Depends(get_db)
):
    manicure = (
        db.query(Manicure)
        .filter(Manicure.id == manicure_id)
        .first()
    )

    if not manicure:
        raise HTTPException(
            status_code=404,
            detail="Manicure não encontrada."
        )

    return manicure


@router.put(
    "/{manicure_id}",
    response_model=ManicureResponse
)
def update_manicure(
    manicure_id: int,
    manicure_data: ManicureUpdate,
    db: Session = Depends(get_db)
):
    manicure = (
        db.query(Manicure)
        .filter(Manicure.id == manicure_id)
        .first()
    )

    if not manicure:
        raise HTTPException(
            status_code=404,
            detail="Manicure não encontrada."
        )

    if manicure_data.name is not None:
        manicure.name = manicure_data.name

    if manicure_data.phone is not None:
        manicure.phone = manicure_data.phone

    db.commit()
    db.refresh(manicure)

    return manicure


@router.delete(
    "/{manicure_id}",
    response_model=ManicureResponse
)
def delete_manicure(
    manicure_id: int,
    db: Session = Depends(get_db)
):
    manicure = (
        db.query(Manicure)
        .filter(Manicure.id == manicure_id)
        .first()
    )

    if not manicure:
        raise HTTPException(
            status_code=404,
            detail="Manicure não encontrada."
        )

    # Anonimização dos dados conforme LGPD
    manicure.name = "Manicure anonimizada"
    manicure.phone = f"ANONIMIZADO-{manicure.id}"
    manicure.active = False

    db.commit()
    db.refresh(manicure)

    return manicure
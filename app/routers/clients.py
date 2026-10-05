from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate, ClientResponse


router = APIRouter(
    prefix="/api/clients",
    tags=["Clients"]
)


@router.post(
    "/",
    response_model=ClientResponse,
    status_code=status.HTTP_201_CREATED
)
def create_client(
    client: ClientCreate,
    db: Session = Depends(get_db)
):
    existing_client = (
        db.query(Client)
        .filter(Client.phone == client.phone)
        .first()
    )

    if existing_client:
        raise HTTPException(
            status_code=400,
            detail="Cliente já cadastrado."
        )

    new_client = Client(
        name=client.name,
        phone=client.phone,
        consent_whatsapp=client.consent_whatsapp,
        active=True
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client


@router.get(
    "/",
    response_model=list[ClientResponse]
)
def list_clients(
    db: Session = Depends(get_db)
):
    return db.query(Client).all()


@router.get(
    "/{client_id}",
    response_model=ClientResponse
)
def get_client(
    client_id: int,
    db: Session = Depends(get_db)
):
    client = (
        db.query(Client)
        .filter(Client.id == client_id)
        .first()
    )

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    return client


@router.put(
    "/{client_id}",
    response_model=ClientResponse
)
def update_client(
    client_id: int,
    client_data: ClientUpdate,
    db: Session = Depends(get_db)
):
    client = (
        db.query(Client)
        .filter(Client.id == client_id)
        .first()
    )

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    if client_data.phone is not None:
        existing_client = (
            db.query(Client)
            .filter(
                Client.phone == client_data.phone,
                Client.id != client_id
            )
            .first()
        )

        if existing_client:
            raise HTTPException(
                status_code=400,
                detail="Telefone já cadastrado para outro cliente."
            )

    if client_data.name is not None:
        client.name = client_data.name

    if client_data.phone is not None:
        client.phone = client_data.phone

    if client_data.consent_whatsapp is not None:
        client.consent_whatsapp = client_data.consent_whatsapp

    db.commit()
    db.refresh(client)

    return client
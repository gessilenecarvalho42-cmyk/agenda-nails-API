from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import clients, manicures, services, appointments, feedbacks, notifications, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Agenda Nails API",
    description="API REST para gerenciamento de clientes, manicures, serviços, agendamentos, feedbacks e notificações do Agenda Nails.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(clients.router)
app.include_router(manicures.router)
app.include_router(services.router)
app.include_router(appointments.router)
app.include_router(feedbacks.router)
app.include_router(notifications.router)

@app.get("/")
def root():
    return {"message": "Agenda Nails API funcionando!"}

@app.get("/health")
def health():
    return {"status": "ok"}

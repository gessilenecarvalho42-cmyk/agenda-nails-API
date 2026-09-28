from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import (
    appointments,
    auth,
    clients,
    feedbacks,
    manicures,
    notifications,
    services,
)

# Cria as tabelas no banco de dados se não existirem
Base.metadata.create_all(bind=engine)

# Instância do FastAPI com configurações para corrigir o redirecionamento e deep linking do Swagger UI
app = FastAPI(
    title="Agenda Nails API",
    description=(
        "API REST para gerenciamento de clientes, manicures, serviços,"
        " agendamentos, feedbacks e notificações do Agenda Nails."
    ),
    version="1.0.0",
    redirect_slashes=False,  # Impede o FastAPI de redirecionar forçadamente URLs com ou sem barra no final
    swagger_ui_parameters={
        "deepLinking": False
    },  # Impede que o Swagger altere o hash da URL (docs#/) ao abrir/testar rotas
)

# Configuração do Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão dos Roteadores da Aplicação
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
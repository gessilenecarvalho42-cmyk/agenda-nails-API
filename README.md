Agenda Nails — Back-End 

API Back-End do sistema Agenda Nails, desenvolvido como parte do Projeto Integrador.

Sobre o projeto

O Agenda Nails é um sistema de agendamento de serviços de manicure. O Back-End é responsável pelo gerenciamento dos dados e pelas regras de negócio da aplicação.

Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Supabase
- Swagger / OpenAPI

Funcionalidades da API

- Cadastro e gerenciamento de clientes
- Cadastro e gerenciamento de manicures
- Cadastro e gerenciamento de serviços
- Gerenciamento de agendamentos
- Feedbacks
- Notificações
- Cancelamento de agendamentos
- Verificação de disponibilidade de horários

Banco de dados

A aplicação utiliza PostgreSQL, hospedado no Supabase.

Documentação da API

A API possui documentação interativa através do Swagger/OpenAPI, permitindo visualizar e testar os endpoints.

Execução do projeto

Instale as dependências:

pip install -r requirements.txt

Execute a API:

uvicorn app.main:app --reload

A documentação do Swagger pode ser acessada pelo endereço:

http://127.0.0.1:8000/docs

Projeto Integrador

Este Back-End corresponde à etapa de desenvolvimento da API do Projeto Integrador 2, dando continuidade ao projeto desenvolvido anteriormente.

Projeto desenvolvido para fins acadêmicos.

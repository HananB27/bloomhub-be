<!-- gardener-constitution-proposal: v1 -->
# Gardener Domain

## Domain

- Gardener should keep changes within this project's domain. Flag work that introduces features outside it.
- In-domain: `web-backend`.
- In-domain: `api-development`.
- In-domain: `multi-tenancy`.
- In-domain: `ai-integration`.
- Capability: User authentication with JWT via djangorestframework-simplejwt.
- Capability: CORS support for cross-origin requests.
- Capability: Multi-tenant data isolation (tenants directory suggests django-tenants or similar).
- Capability: RESTful API built with Django REST Framework.
- Capability: AI/LLM integration using LangChain and LangChain-OpenAI.
- Capability: File upload handling (media directory).
- Capability: Database support for both SQLite and PostgreSQL.
- Capability: Test suite with pytest-django.

## Out-of-Domain Examples

- Frontend UI components
- Real-time messaging or WebSocket services
- Machine learning model training
- Non-web backend services (e.g., desktop app, CLI tool without Django)
- Game logic or interactive simulations

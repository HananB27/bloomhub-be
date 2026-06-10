<!-- gardener-constitution-proposal: v1 -->
# Gardener Domain

## Domain

- Gardener should keep changes within this project's domain. Flag work that introduces features outside it.
- In-domain: `web-backend`.
- In-domain: `multi-tenant`.
- In-domain: `ai/llm`.
- Capability: Django REST API with JWT authentication.
- Capability: CORS handling for cross-origin requests.
- Capability: Multi-tenant database architecture (tenants directory).
- Capability: Integration with LLM via LangChain (langchain, langchain-openai).
- Capability: Local development with SQLite or PostgreSQL.
- Capability: Docker-based PostgreSQL setup for staging/production parity.
- Capability: Database migration and management for PostgreSQL on macOS, Linux, Windows.
- Capability: Automated testing with pytest-django.
- Capability: Media file handling (media directory).
- Capability: Configurable environment variables via .env.

## Out-of-Domain Examples

- Frontend user interface (UI/UX)
- iOS or Android mobile app
- Real-time chat or WebSocket server
- Payment processing or billing system
- GraphQL API
- Desktop application
- Image or video processing pipeline

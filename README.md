# Incident AI

A full-stack incident management system built as a learning project to refresh and deepen skills in FastAPI, PostgreSQL, SQLAlchemy, Alembic, Next.js, and Docker.

---

## Why I built this

This project came after a "training wheels" phase where I built a basic blogging API to get familiar with the stack. Incident AI is the real thing — a more complete, multi-layered application built one phase at a time, with each phase introducing new concepts on top of what came before.

The goal wasn't to ship a product. It was to understand *why* each piece exists and how they fit together.

---

## What's inside

### Backend — FastAPI + PostgreSQL

A REST API built with FastAPI, running in Docker, backed by a real PostgreSQL database.

**Endpoints:**
- `GET /health` — health check
- `POST /incidents` — create an incident
- `GET /incidents` — list all incidents
- `POST /ask` — stub endpoint for future LLM integration
- `POST /documents/ingest` — stub endpoint for future RAG pipeline

**Auth:** All endpoints (except `/health`) are protected by a simple API key passed via the `x-api-key` header.

**Database:** SQLAlchemy ORM with an `Incident` model. Started with in-memory storage, then replaced it with a real Postgres database as Phase 2.

**Migrations:** Alembic tracks schema changes. Running `alembic upgrade head` applies all migrations to the database.

---

### Frontend — Next.js (App Router)

A minimal UI built with Next.js 16 and Tailwind CSS.

**Pages:**
- `/` — Dashboard: fetches all incidents from the API and displays them as cards
- `/incidents/[id]` — Incident detail: dynamic route that shows full details for a single incident
- `/ask` — Chat page: form that POSTs a question to `/ask` and displays the response

**Key concepts practiced:**
- `async` server components — fetching data directly in page components without `useEffect`
- Dynamic routing with `[id]` folders
- Client components with `"use client"` and `useState` for interactive forms
- `<Link>` for client-side navigation
- CORS middleware on the API to allow browser requests from a different port

---

### Infrastructure — Docker Compose

All services run together with a single `docker compose up --build`:

| Service    | Port | Description              |
|------------|------|--------------------------|
| `api`      | 8000 | FastAPI backend          |
| `db`       | 5432 | PostgreSQL database      |
| `frontend` | 3000 | Next.js frontend         |

Services communicate by name inside Docker (e.g. `http://api:8000`). Server-side Next.js components use this internal URL; browser-side client components use `http://localhost:8000`.

---

## Phases

| Phase | What | Status |
|-------|------|--------|
| 1 | Backend APIs — health, incidents, ask stub, document ingest, API key auth | Done |
| 2 | Real database — Postgres, SQLAlchemy models, Alembic migrations | Done |
| 3 | Next.js UI — dashboard, incident detail, chat page, Docker wiring | Done |
| 4 | LLM integration — wire `/ask` to a real language model | Upcoming |
| 5 | RAG pipeline — embed and index documents for context-aware answers | Upcoming |

---

## Running locally

```bash
docker compose up --build
```

Then open:
- Frontend: http://localhost:3000
- API docs: http://localhost:8000/docs

API key: `secret-key-123`

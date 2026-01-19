# 🚀 **AI Chatbot API – DevOps Capstone**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-05998b?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?logo=postgresql&logoColor=white)](https://postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?logo=docker&logoColor=white)](https://docker.com/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue?logo=githubactions&logoColor=white)](./.github/workflows/ci.yml)

**DevOps-focused capstone** showcasing production CI/CD for a real FastAPI backend.  
Automated tests, Docker image builds, registry pushes, and Cloud Run deployments for **staging + production**.

> ✅ **Tests on every push** · 🐳 **Dockerized** · ☁️ **Cloud Run** · 🔐 **Secrets managed** · 📊 **Health checks**

**Live API Docs:**  
[![Open Docs](https://img.shields.io/badge/Open%20Docs-Live%20Swagger-1f9d6a?style=for-the-badge)](https://p01--ai-chatbot-api--zn54zt65xhrv.code.run/docs)

---

## 📌 **Table of Contents**
- [🏗️ Architecture](#️-architecture)
- [🔎 Observability](#-observability)
- [🧪 CI Pipeline](#-ci-pipeline)
- [🚀 CD Pipelines](#-cd-pipelines)
- [🔐 Secrets Management](#-secrets-management)
- [📦 Docker](#-docker)
- [🧪 Local Testing](#-local-testing)
- [↩️ Rollback Strategy](#️-rollback-strategy)

---

## 🏗️ **Architecture**
```
GitHub -> GitHub Actions -> Artifact Registry -> Cloud Run (staging/prod)
                                    |
                                 PostgreSQL
```

Key components:
- FastAPI backend under `app/`
- Alembic migrations
- Docker image built for Cloud Run
- CI/CD workflows in `.github/workflows/`

---

## 🔎 **Observability**
- **Health check:** `GET /health`
- Structured, stdout logging (Cloud Run friendly)

---

## 🧪 **CI Pipeline**
Workflow: `.github/workflows/ci.yml`
- Runs on every push and pull request
- Installs dependencies
- Executes `pytest`
- Fails fast on any error

---

## 🚀 **CD Pipelines**
### Staging
Workflow: `.github/workflows/deploy-staging.yml`
- Trigger: push to `main`
- Build image, tag with commit SHA
- Push to Google Artifact Registry
- Deploy to **Cloud Run (staging)**

### Production
Workflow: `.github/workflows/deploy-production.yml`
- Trigger: GitHub Release (published)
- Build image, tag with release version
- Push to Google Artifact Registry
- Deploy to **Cloud Run (production)**

---

## 🔐 **Secrets Management**
All sensitive values are injected via **GitHub Secrets** and scoped by **GitHub Environments**:
- `GCP_PROJECT_ID`
- `GCP_REGION`
- `GCP_SERVICE_ACCOUNT_KEY`
- `DATABASE_URL`
- `OPENAI_API_KEY`
- `JWT_SECRET_KEY`

Use **environment-specific secrets** for `staging` and `production` to isolate configs.

---

## 📦 **Docker**
Production-grade Docker image:
- Multi-stage build
- Non-root user
- Health check wired to `/health`
- Minimal slim base image

---

## 🧪 **Local Testing**
```bash
pip install -r requirements.txt
pytest
```

---

## ↩️ **Rollback Strategy**
Cloud Run retains prior revisions. Roll back by re-deploying a previous image tag
or selecting an earlier revision in Cloud Run.

_Pipeline trigger note: update to validate CI/CD._


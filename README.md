# Undergoing stack changes and updates. Updated will be pushed soon.

# 🧠 Recallify

> A personal knowledge base + smart reminder system for knowledge workers, students, and lifelong learners.

Recallify helps you remember and retrieve what matters — through markdown notes, smart tagging, semantic search, and intelligent reminders.

---
## ✨ Features

- 📝 Markdown-based notes with versioning and tagging
- 🔍 Full-text + semantic search (FAISS + embeddings)
- ⏰ Time and context-based reminders (Email, Telegram)
- 🧠 AI assistant for related notes + summaries
- 📚 Notebook/topic organization
- 🔐 OAuth login (GitHub, Google)
- 📱 Responsive, PWA-ready UI

---

## 🛠 Tech Stack

**Frontend**
- Next.js (App Router)
- Tailwind CSS

**Backend**
- FastAPI
- SQLModel ORM
- Celery + Redis
- PostgreSQL (Neon/Supabase)

**AI/ML**
- `sentence-transformers` (MiniLM)
- FAISS vector index

**Notifications**
- Gmail SMTP
- Telegram Bot

**Infra**
- Docker + Docker Compose
- GitHub Actions (CI)
- Vercel (Frontend) + Render (API)

---

## 🚀 Getting Started

### 1. Clone & Setup

```bash
git clone https://github.com/your-username/recallify.git
cd recallify
```

### 2. Run with Docker

```bash
docker-compose up --build
```

This will start:
- FastAPI backend on `http://localhost:8000`
- Redis
- PostgreSQL
- Celery worker

### 3. Dev Mode (Optional)

Frontend:
```bash
cd web
npm install
npm run dev
```

Backend:
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

### 4. Environment Variables

Create `.env` files in `/web` and `/api`. Example for backend:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/recallify
SECRET_KEY=your_jwt_secret
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_password
TELEGRAM_BOT_TOKEN=your_token
```

## 📐 Architecture

See [SPEC-1-Recallify](./docs/architecture.md) for full design spec.

## 📦 Folder Structure

```
recallify/
├── api/      # FastAPI app
├── web/      # Next.js frontend
```

## 🧪 Testing

Backend:
```bash
pytest
```

Frontend:
```bash
npm run test
```

## 📄 License

MIT

---

## 👨‍💻 Author
### Vikram Ramji Iyer
📧 vikramramji24@gmail.com

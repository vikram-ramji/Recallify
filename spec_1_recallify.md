# SPEC-1-Recallify

## Background

In an era of information overload, knowledge workers and learners increasingly struggle with organizing and recalling the vast amount of content they consume—articles, insights, quotes, tasks, links, and more. Traditional note-taking tools often fail to surface timely or contextually relevant information. “Recallify” aims to solve this by combining structured knowledge capture with smart, AI-driven recall and reminder mechanisms. It enhances personal memory through intelligent tagging, semantic search, and proactive nudges based on user behavior and context.

## Requirements

### Must Have
- Create, edit, delete, and archive notes with markdown support
- Tagging system (manual + AI-suggested tags)
- Smart reminders (time-based, recurring)
- Full-text + semantic search across notes
- AI assistant: related note suggestions, summarization
- User authentication via Google or GitHub (OAuth)
- REST API with OpenAPI docs
- Responsive UI with rich note editor
- PostgreSQL with versioned notes and tagging schema
- File attachments (stored in local or cloud)
- Notification system (Email or Telegram-based)
- Deployed and Dockerized (CI/CD with GitHub Actions)

### Should Have
- Notebook/topic collections (group + nest notes)
- Calendar view of upcoming reminders
- Smart reminder triggers (e.g., context-based)
- Embedding-powered semantic search (via local model + FAISS)
- User settings for theme, integrations

### Could Have
- Push notifications (web or mobile)
- Rephrase old notes in different styles (AI-powered)
- Cross-device sync using background jobs
- Export/backup data as Markdown/JSON

### Won’t Have (MVP)
- Real-time collaboration or multi-user support
- Third-party sync (Notion, Roam, etc.)
- Monetization (premium plans, sharing with others)

## Method

### Notes Management Module

- Markdown-rich notes with versioning
- Manual + AI-suggested tags
- Attachments

**Tables:** users, notes, note_versions, tags, note_tags, attachments

### Search & Filtering

- PostgreSQL full-text search + FAISS semantic search
- sentence-transformers (`all-MiniLM-L6-v2`)
- saved_filters table for saved queries

### Smart Reminder System

- Celery + Redis for scheduling
- One-time + recurring reminders
- Context triggers processed asynchronously
- Email (SMTP) and Telegram Bot notifications

**Tables:** reminders

### AI Assistant (Recall Engine)

- Suggest notes to revisit (recency, tags, patterns)
- Summarization/rephrasing (local LLM or mocked)
- Inline related note suggestions using FAISS

### Notebook / Topic Collections

- Notebooks with nesting, pinning, exporting

**Tables:** notebooks, note_notebook

### User Management & Sync

- OAuth + JWT
- User preferences (notification channel, theme)

**Tables:** user_preferences

### System Infrastructure

| Layer            | Technology                           |
|------------------|----------------------------------------|
| Frontend         | Next.js App Router, Tailwind, PWA-ready |
| API Backend      | FastAPI + SQLModel + Uvicorn           |
| Auth             | OAuth (Google, GitHub) + JWT           |
| DB               | PostgreSQL (Neon or Supabase)          |
| Task Queue       | Celery + Redis                         |
| Semantic AI      | sentence-transformers + FAISS          |
| Summarization    | Local LLM via Ollama or mock summaries |
| Notifications    | SMTP (Gmail) + Telegram Bot            |
| File Storage     | Local `/uploads` or Cloud              |
| Infra            | Docker Compose + GitHub Actions CI/CD  |
| Deployment       | Vercel (web), Render (API), Neon (DB)  |

## Implementation

1. Project Setup
2. Auth + User Management
3. Notes Core Features
4. Search (Text + Semantic)
5. Smart Reminders
6. AI Assistant
7. Notebook / Topic Collections
8. Final Polish

## Milestones

### Milestone 1: Project Foundation
- GitHub repo setup, Docker Compose, CI/CD

### Milestone 2: Auth + User Profiles
- OAuth login, JWT, user table, auth UI

### Milestone 3: Notes Core Features
- Notes CRUD, markdown editor, tags, attachments, versioning

### Milestone 4: Search (Text + Semantic)
- PostgreSQL full-text, FAISS, search UI

### Milestone 5: Reminders System
- Reminder creation UI, Celery, notifications, calendar view

### Milestone 6: AI Assistant (Recall Engine)
- Related note suggestions, summarization, smart tags

### Milestone 7: Notebooks & Collections
- Notebooks, nesting, pinning, exporting

### Milestone 8: Polish & Deploy
- Settings, theme, PWA, deploy to Vercel/Render/Neon

## Gathering Results

### Success Metrics
- User can manage notes, search, receive reminders
- Semantic recall and suggestions feel relevant
- Deployed and mobile-responsive

### Evaluation Criteria
- Functionality: full module flow works
- UX: polished and responsive
- AI: suggestions and summaries add value
- Infra: reminders reliable, CI green
- Code: clean, testable, documented

### Portfolio Tips
- Record short demo
- Include README + system diagram
- Link to live version

## Need Professional Help in Developing Your Architecture?

Please contact me at [sammuti.com](https://sammuti.com) :)


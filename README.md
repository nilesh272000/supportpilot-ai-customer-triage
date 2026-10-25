# SupportPilot AI — Customer Support Triage

Production-oriented AI customer-support triage platform for classifying incoming tickets, estimating urgency, routing to the right team, extracting structured issue details, and generating concise agent-ready summaries.

## Features
- AI-assisted ticket classification
- Intent/category detection
- Priority and urgency scoring
- Team/queue routing
- Sentiment detection
- SLA-aware triage
- Structured ticket enrichment
- Optional OpenAI integration point
- FastAPI REST API + Swagger
- Browser dashboard
- Demo ticket dataset
- Unit tests
- No Docker
- No secrets committed

## Run
```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload --port 8080
```

Open `http://127.0.0.1:8080` and Swagger at `http://127.0.0.1:8080/docs`.

This is an independent implementation inspired by the high-level customer-support triage problem space, not a copy of the reference repository.

from pathlib import Path
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from services.triage import triage_ticket

app = FastAPI(title="SupportPilot AI", version="1.0.0")
BASE = Path(__file__).parent
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE / "templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health():
    return {"status": "ok", "service": "supportpilot-ai"}

@app.post("/api/triage")
def triage(payload: dict):
    return triage_ticket(payload)

@app.get("/api/demo-tickets")
def demo_tickets():
    return json.loads((BASE / "demo_tickets.json").read_text(encoding="utf-8"))

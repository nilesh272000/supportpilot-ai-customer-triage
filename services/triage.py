import re

INTENTS = {
    "billing": ["invoice", "charge", "charged", "payment", "refund", "subscription", "billing"],
    "technical": ["error", "bug", "crash", "failed", "failure", "not working", "timeout", "login"],
    "account": ["account", "password", "profile", "access", "verification"],
    "delivery": ["delivery", "shipment", "tracking", "order", "package", "late"],
    "security": ["fraud", "hacked", "unauthorized", "security", "stolen"],
}
TEAM_MAP = {"billing":"Billing Operations", "technical":"Technical Support", "account":"Account Support", "delivery":"Order & Delivery", "security":"Trust & Safety", "general":"Customer Support"}

def _sentiment(text):
    t=text.lower(); neg=["angry","unacceptable","terrible","frustrated","worst","urgent","scam"]; pos=["thanks","thank you","great","appreciate"]
    if sum(w in t for w in neg)>=2:return "very_negative"
    if any(w in t for w in neg):return "negative"
    if any(w in t for w in pos):return "positive"
    return "neutral"

def _intent(text):
    t=text.lower(); scores={k:sum(w in t for w in words) for k,words in INTENTS.items()}; best=max(scores,key=scores.get)
    return best if scores[best] else "general"

def _priority(text,intent,sentiment):
    t=text.lower()
    if any(x in t for x in ["fraud","hacked","unauthorized","security breach","data leak"]): return "P0"
    if any(x in t for x in ["urgent","asap","blocked","production down","cannot access"]) or sentiment=="very_negative": return "P1"
    if intent in {"technical","billing"}: return "P2"
    return "P3"

def triage_ticket(payload):
    text=str(payload.get("message") or payload.get("description") or "").strip()
    if not text:return {"error":"message is required"}
    intent=_intent(text); sentiment=_sentiment(text); priority=_priority(text,intent,sentiment); team=TEAM_MAP[intent]
    sla={"P0":"15 minutes","P1":"1 hour","P2":"4 hours","P3":"1 business day"}[priority]
    clean=re.sub(r"\s+"," ",text).strip()
    return {"ticket_id":payload.get("ticket_id","NEW-TICKET"),"intent":intent,"priority":priority,"sentiment":sentiment,"assigned_team":team,"suggested_sla":sla,"summary":f"{priority} {intent} issue routed to {team}. Customer report: {clean[:240]}","confidence":0.91 if intent!="general" else 0.63}

from fastapi.testclient import TestClient
from app import app
client=TestClient(app)
def test_health(): assert client.get('/health').json()['status']=='ok'
def test_triage():
    data=client.post('/api/triage',json={'message':'I was charged twice and need a refund'}).json()
    assert data['intent']=='billing'; assert data['assigned_team']=='Billing Operations'

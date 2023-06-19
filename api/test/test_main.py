from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_base_user():
    responses = client.get("/users/")
    assert responses.status_code == 200
    assert responses.json() == {
        "msg" : "c'est cool"
    }
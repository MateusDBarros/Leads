import pytest
from main import app, db, Person

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://:memory:'
    with  app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            with app.app_context():
                db.drop_all()

def test_post(client):
    lead_data = {
        'nome': 'Mateus',
        'email': 'teste.1@example.com',
        'proposta': 'Gostaria de mais informações sobre um de seus modelos de IA'
    }
    response = client.post('/api', json=lead_data)

    assert response.status_code == 201
    data = response.get_json()

    assert data["nome"] == lead_data["nome"]
    assert data["email"] == lead_data["email"]
    assert data["proposta"] == lead_data["proposta"]


def test_get_leads(client):
    response = client.get("/api")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)


def test_delete_lead(client):

    lead_data = {
        "nome": "Alice Doe",
        "email": "alice.doe@example.com",
        "proposta": "Estou interessada em um orçamento"
    }
    post_response = client.post("/api", json=lead_data)
    lead_id = post_response.get_json()["id"]


    delete_response = client.delete(f"/api/{lead_id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/api/{lead_id}")
    assert get_response.status_code == 404
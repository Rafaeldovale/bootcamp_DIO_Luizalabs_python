import pytest
from httpx import AsyncClient
from workout_api.main import app

@pytest.mark.asyncio
async def test_create_athlete_success():
    athlete_data = {
        "nome": "João Silva",
        "cpf": "12345678900",
        "idade": 25,
        "peso": 80.0,
        "altura": 1.80,
        "sexo": "M"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/atletas/", json=athlete_data)
    
    assert response.status_code == 201
    assert response.json()["nome"] == "João Silva"
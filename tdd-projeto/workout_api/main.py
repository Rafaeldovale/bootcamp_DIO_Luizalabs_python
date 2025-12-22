from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="WorkoutAPI")


class AthleteOut(BaseModel):
    nome: str
    cpf: str

@app.get("/atletas/", response_model=List[AthleteOut])
async def get_athletes():
    return [] # Retorna lista vazia 
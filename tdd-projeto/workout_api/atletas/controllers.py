from fastapi import APIRouter, status, HTTPException
from workout_api.atletas.schemas import Atleta
from workout_api.db.database import db # Sua conexão com o Motor

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_athlete(athlete: Atleta):
    # Transforma o objeto Pydantic em dicionário para o Mongo
    athlete_dict = athlete.model_dump() 
    
    # Insere na coleção 'athletes'
    result = await db.athletes.insert_one(athlete_dict)
    
    return {"id": str(result.inserted_id), **athlete_dict}
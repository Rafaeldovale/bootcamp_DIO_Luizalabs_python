from fastapi import APIRouter
from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categorias
from workout_api.centro_treinamento.controller import router as categorias

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atleta', tags=['atletas'])
api_router.include_router(atleta, prefix='/categorias', tags=['categorias'])
api_router.include_router(atleta, prefix='/centro_treinamento', tags=['centro_treinamento'])
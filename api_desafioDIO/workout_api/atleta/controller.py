import datetime
from sqlalchemy.future import select
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body

from workout_api.atleta.schemas import AtletaIn, AtletaOut
from workout_api.categorias.models import CategoriaModel
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.atleta.models import AtletaModel
router = APIRouter()

@router.post(
        '/',
        summary='Criar novo atleta',
        status_code=status.HTTP_201_CREATED,
        response_model=AtletaOut
)
async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=atleta_in))).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            datail=f'Categoria não encontrada no id {id}'
        )
    atleta_out = AtletaOut(id-uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
    atleta_model = AtletaModel(**atleta_out.model_dump())

    db_session.add(atleta_model)
    await db_session.commit()

    return atleta_out
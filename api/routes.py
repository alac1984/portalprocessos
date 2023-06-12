from fastapi import APIRouter, Depends
from models.grupo import Grupo
from db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from repository.grupo import repo_retrieve_grupo


router = APIRouter()


@router.get("/grupo/{grupo_id}", response_model=Grupo)
async def retrieve_grupo(grupo_id: int, session: AsyncSession = Depends(get_session)):
    result = await repo_retrieve_grupo(grupo_id, session)

    return result

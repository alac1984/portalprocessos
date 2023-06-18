from typing import Optional
from fastapi import APIRouter, Depends
from models.grupo import Grupo
from models.macroprocesso import Macroprocesso
from db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from repository.grupo import repo_retrieve_grupo
from repository.macroprocesso import repo_retrieve_macroprocesso


router = APIRouter()


@router.get("/grupos/{grupo_id}", response_model=Optional[Grupo])
async def retrieve_grupo(
    grupo_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Grupo]:
    result = await repo_retrieve_grupo(grupo_id, session)

    return result


@router.get(
    "/macroprocessos/{macroprocesso_id}", response_model=Optional[Macroprocesso]
)
async def retrieve_macroprocesso(
    macroprocesso_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Macroprocesso]:
    result = await repo_retrieve_macroprocesso(macroprocesso_id, session)

    return result

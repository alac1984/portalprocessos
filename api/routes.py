from typing import Optional
from fastapi import APIRouter, Depends
from models.grupo import Grupo, GrupoCreate
from models.macroprocesso import Macroprocesso, MacroprocessoCreate
from db.session import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from repository.grupo import (
    repo_retrieve_grupo,
    repo_create_grupo,
    repo_retrieve_all_grupo,
)
from repository.macroprocesso import (
    repo_retrieve_macroprocesso,
    repo_create_macroprocesso,
)


router = APIRouter()


@router.get("/grupos/{grupo_id}", response_model=Optional[Grupo])
async def retrieve_grupo(
    grupo_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Grupo]:
    result = await repo_retrieve_grupo(grupo_id, session)

    return result


@router.get("/grupos", response_model=Optional[list[Grupo]])
async def retrieve_all_grupo(
    session: AsyncSession = Depends(get_session),
) -> Optional[list[Grupo]]:
    result = await repo_retrieve_all_grupo(session)

    return result


@router.post("/grupos", response_model=Grupo)
async def create_grupo(
    grupo_create: GrupoCreate, session: AsyncSession = Depends(get_session)
) -> Grupo:
    grupo = await repo_create_grupo(grupo_create, session)

    return grupo


@router.get(
    "/macroprocessos/{macroprocesso_id}", response_model=Optional[Macroprocesso]
)
async def retrieve_macroprocesso(
    macroprocesso_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Macroprocesso]:
    result = await repo_retrieve_macroprocesso(macroprocesso_id, session)

    return result


@router.post("/macroprocessos", response_model=Macroprocesso)
async def create_macroprocesso(
    macro_create: MacroprocessoCreate, session: AsyncSession = Depends(get_session)
) -> Macroprocesso:
    macro = await repo_create_macroprocesso(macro_create, session)

    return macro

from typing import Optional
from fastapi import APIRouter, Depends
from models.grupo import Grupo, GrupoCreate
from models.macroprocesso import Macroprocesso, MacroprocessoCreate
from models.microprocesso import Microprocesso, MicroprocessoCreate
from db.session import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from repository.grupo import (
    repo_retrieve_grupo,
    repo_create_grupo,
    repo_retrieve_all_grupo,
    repo_delete_grupo,
)
from repository.macroprocesso import (
    repo_retrieve_macroprocesso,
    repo_create_macroprocesso,
    repo_retrieve_all_macroprocesso,
    repo_delete_macroprocesso,
)
from repository.microprocesso import (
    repo_retrieve_microprocesso,
    repo_create_microprocesso,
    repo_retrieve_all_microprocesso,
    repo_delete_microprocesso,
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


@router.delete("/grupos/{grupo_id}", response_model=Optional[Grupo])
async def delete_grupo(
    grupo_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Grupo]:
    result = await repo_delete_grupo(grupo_id, session)

    return result


@router.get(
    "/macroprocessos/{macroprocesso_id}", response_model=Optional[Macroprocesso]
)
async def retrieve_macroprocesso(
    macroprocesso_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Macroprocesso]:
    result = await repo_retrieve_macroprocesso(macroprocesso_id, session)

    return result


@router.get("/macroprocessos", response_model=Optional[list[Macroprocesso]])
async def retrieve_all_macroprocesso(
    session: AsyncSession = Depends(get_session),
) -> Optional[list[Macroprocesso]]:
    results = await repo_retrieve_all_macroprocesso(session)

    return results


@router.post("/macroprocessos", response_model=Macroprocesso)
async def create_macroprocesso(
    macro_create: MacroprocessoCreate, session: AsyncSession = Depends(get_session)
) -> Macroprocesso:
    macro = await repo_create_macroprocesso(macro_create, session)

    # TODO: treat error in case grupo_id not present in database (as returned by repo)

    return macro


@router.delete(
    "/macroprocessos/{macroprocesso_id}", response_model=Optional[Macroprocesso]
)
async def delete_macroprocesso(
    macroprocesso_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Macroprocesso]:
    result = await repo_delete_macroprocesso(macroprocesso_id, session)

    return result


@router.get("/microprocessos/{micro_id}", response_model=Optional[Microprocesso])
async def retrieve_microprocesso(
    micro_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Microprocesso]:
    result = await repo_retrieve_microprocesso(micro_id, session)

    return result


@router.post("/microprocessos", response_model=Microprocesso)
async def create_microprocesso(
    micro_create: MicroprocessoCreate, session: AsyncSession = Depends(get_session)
) -> Microprocesso:
    micro = await repo_create_microprocesso(micro_create, session)

    # TODO: treat error if macroprocesso_id does not exist in database (as repo returns it)  # noqa

    return micro


@router.get("/microprocessos", response_model=Optional[list[Microprocesso]])
async def retrieve_all_microprocesso(
    session: AsyncSession = Depends(get_session),
) -> Optional[list[Microprocesso]]:
    results = await repo_retrieve_all_microprocesso(session)

    return results


@router.delete(
    "/microprocessos/{microprocesso_id}", response_model=Optional[Microprocesso]
)
async def delete_microprocesso(
    microprocesso_id: int, session: AsyncSession = Depends(get_session)
) -> Optional[Microprocesso]:
    result = await repo_delete_microprocesso(microprocesso_id, session)

    return result

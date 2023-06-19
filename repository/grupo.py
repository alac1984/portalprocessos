from typing import Optional
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from models.grupo import Grupo, GrupoCreate


async def repo_retrieve_grupo(grupo_id: int, session: AsyncSession) -> Optional[Grupo]:
    result = await session.get(Grupo, grupo_id)

    return result


async def repo_retrieve_all_grupo(session: AsyncSession) -> Optional[list[Grupo]]:
    statement = select(Grupo)
    results = await session.exec(statement)  # type: ignore
    grupos = results.all()

    return grupos


async def repo_create_grupo(grupo_create: GrupoCreate, session: AsyncSession) -> Grupo:
    grupo = Grupo(nome=grupo_create.nome, nome_exibicao=grupo_create.nome_exibicao)

    session.add(grupo)
    await session.commit()

    return grupo


async def repo_delete_grupo(grupo_id: int, session: AsyncSession) -> Optional[Grupo]:
    grupo = await session.get(Grupo, grupo_id)

    if grupo is not None:
        await session.delete(grupo)
        await session.commit()

    return grupo

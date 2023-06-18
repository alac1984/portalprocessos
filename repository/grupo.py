from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from models.grupo import Grupo, GrupoCreate


async def repo_retrieve_grupo(grupo_id: int, session: AsyncSession) -> Optional[Grupo]:
    result = await session.get(Grupo, grupo_id)

    return result


async def repo_create_grupo(grupo_create: GrupoCreate, session: AsyncSession) -> Grupo:
    grupo = Grupo(nome=grupo_create.nome, nome_exibicao=grupo_create.nome_exibicao)

    session.add(grupo)
    await session.commit()

    return grupo

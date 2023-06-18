from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from models.grupo import Grupo


async def repo_retrieve_grupo(grupo_id: int, session: AsyncSession) -> Optional[Grupo]:
    result = await session.get(Grupo, grupo_id)

    return result

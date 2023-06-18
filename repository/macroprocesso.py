from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from models.macroprocesso import Macroprocesso


async def repo_retrieve_macroprocesso(
    macroprocesso_id: int, session: AsyncSession
) -> Optional[Macroprocesso]:
    result = await session.get(Macroprocesso, macroprocesso_id)

    return result

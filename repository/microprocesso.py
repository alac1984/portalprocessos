from typing import Optional
from sqlmodel.ext.asyncio.session import AsyncSession
from models.microprocesso import Microprocesso


async def repo_retrieve_microprocesso(
    macroprocesso_id: int, session: AsyncSession
) -> Optional[Microprocesso]:
    result = await session.get(Microprocesso, macroprocesso_id)

    return result

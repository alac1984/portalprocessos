from typing import Optional
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from models.microprocesso import Microprocesso, MicroprocessoCreate


async def repo_retrieve_microprocesso(
    macroprocesso_id: int, session: AsyncSession
) -> Optional[Microprocesso]:
    result = await session.get(Microprocesso, macroprocesso_id)

    return result


async def repo_create_microprocesso(
    micro_create: MicroprocessoCreate, session: AsyncSession
) -> Microprocesso:
    micro = Microprocesso(
        nome=micro_create.nome,
        nome_exibicao=micro_create.nome_exibicao,
        macroprocesso_id=micro_create.macroprocesso_id,
        url=micro_create.url,
    )

    session.add(micro)
    await session.commit()

    return micro


async def repo_retrieve_all_microprocesso(
    session: AsyncSession,
) -> Optional[list[Microprocesso]]:
    statement = select(Microprocesso)
    results = await session.exec(statement)  # type: ignore
    microprocessos = results.all()

    return microprocessos

from sqlmodel import select
from typing import Optional
from sqlmodel.ext.asyncio.session import AsyncSession
from models.macroprocesso import Macroprocesso, MacroprocessoCreate


async def repo_retrieve_macroprocesso(
    macroprocesso_id: int, session: AsyncSession
) -> Optional[Macroprocesso]:
    result = await session.get(Macroprocesso, macroprocesso_id)

    return result


async def repo_retrieve_all_macroprocesso(
    session: AsyncSession,
) -> Optional[list[Macroprocesso]]:
    statement = select(Macroprocesso)
    results = await session.exec(statement)  # type: ignore
    macroprocessos = results.all()

    return macroprocessos


async def repo_create_macroprocesso(
    macro_create: MacroprocessoCreate, session: AsyncSession
) -> Macroprocesso:
    macro = Macroprocesso(
        nome=macro_create.nome,
        nome_exibicao=macro_create.nome_exibicao,
        grupo_id=macro_create.grupo_id,
    )

    session.add(macro)
    await session.commit()

    return macro

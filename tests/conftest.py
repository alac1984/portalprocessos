import pytest_asyncio
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from models.grupo import Grupo  # noqa
from models.macroprocesso import Macroprocesso  # noqa


@pytest_asyncio.fixture(scope="function")
async def test_session():
    DATABASE_URL = (
        "postgresql+asyncpg://test_portalprocessos:a1k8u2@localhost:5433"
        "/test_portalprocessos"
    )
    engine = create_async_engine(DATABASE_URL, echo=True, future=True)

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        grupo1 = Grupo(nome="grupo_teste_01", nome_exibicao="Grupo de Testes 01")
        grupo2 = Grupo(nome="grupo_teste_02", nome_exibicao="Grupo de Testes 02")
        macroprocesso1 = Macroprocesso(
            nome="macro_teste_01", nome_exibicao="Macro de Testes 1", grupo_id=1
        )
        macroprocesso2 = Macroprocesso(
            nome="macro_teste_02", nome_exibicao="Macro de Testes 2", grupo_id=1
        )
        session.add(grupo1)
        session.add(grupo2)
        session.add(macroprocesso1)
        session.add(macroprocesso2)
        await session.commit()

        yield session

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

    await engine.dispose()

import pytest_asyncio
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
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
        grupo1 = Grupo(id=1, nome="grupo_teste", nome_exibicao="Grupo de Testes")
        macroprocesso1 = Macroprocesso(
            id=1, nome="macro_teste", nome_exibicao="Macro de Testes"
        )
        session.add(grupo1)
        session.add(macroprocesso1)
        await session.commit()

        yield session

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

    await engine.dispose()

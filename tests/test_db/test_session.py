import pytest
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from db.session import get_database_url, create_engine, get_session


def test_get_database_url():
    url = get_database_url()
    assert url is not None
    assert isinstance(url, str)


def test_create_engine():
    url = "postgresql+asyncpg://dummy:dummy@dummy:5432/dummy"
    engine = create_engine(url)
    assert engine is not None
    assert isinstance(engine, AsyncEngine)


@pytest.mark.asyncio
async def test_get_session():
    session_gen = get_session()
    session = await session_gen.asend(None)

    assert isinstance(session_gen, AsyncGenerator)
    assert isinstance(session, AsyncSession)

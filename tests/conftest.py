import os
import pytest_asyncio
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()


@pytest_asyncio.fixture(scope="function")
async def test_session():
    DATABASE_URL = os.environ.get("DATABASE_URL")

    engine = create_async_engine(DATABASE_URL, echo=True, future=True)

    session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    yield session

    await engine.dispose()

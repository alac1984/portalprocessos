import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker


load_dotenv()


def get_database_url():
    return os.environ.get("DATABASE_URL")


def create_engine(url: str) -> AsyncEngine:
    return create_async_engine(url, echo=True, future=True)


DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:  # type: ignore
    async with async_session() as session:
        yield session

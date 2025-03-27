from collections.abc import AsyncGenerator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings


if settings.MODE == "TEST":
    DATABASE_URL = "sqlite+aiosqlite:///./test.db"
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = "sqlite+aiosqlite:///./database.db"
    DATABASE_PARAMS = {}


class Base(DeclarativeBase):
    pass


engine = create_async_engine(DATABASE_URL, echo=False, **DATABASE_PARAMS)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

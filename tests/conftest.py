from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from src.config import settings
from src.database import engine, Base
from src.main import app


@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    async def prepare_database():
        if settings.MODE != "TEST":
            raise Exception

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Create a http client."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac


# @pytest_asyncio.fixture(scope="session")
# async def authenticated_client() -> AsyncGenerator[AsyncClient, None]:
#     """Create an authenticated http client."""
#     async with AsyncClient(
#         transport=ASGITransport(app=app),
#         base_url="http://test",
#     ) as ac:
#         data = {"username": "test@test.com", "password": "password"}
#         await ac.post("/auth/token", data=data)
#         yield ac

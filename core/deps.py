from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

#Generator que define o funcionamento da sessão assíncrona, a fecha após o uso.
async def getSession() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()

    
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from gdhub.db import get_session

router = APIRouter(prefix="/healthz", tags=["health"])

@router.get("")
async def healthz(session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        await session.execute("SELECT 1")
        db_status = "ok"
    except SQLAlchemyError:
        db_status = "error"
    return {"status": "ok", "db": db_status}

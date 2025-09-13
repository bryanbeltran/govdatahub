from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from gdhub.db import get_session
from gdhub.models import Inmate

router = APIRouter(prefix="/inmates", tags=["inmates"])

@router.get("/")
async def list_inmates(session: Annotated[AsyncSession, Depends(get_session)]):
    result = await session.execute(select(Inmate))
    inmates = result.scalars().all()
    return [
        {
            "id": inmate.id,
            "first_name": inmate.first_name,
            "last_name": inmate.last_name,
            "dob": inmate.dob,
        }
        for inmate in inmates
    ]

from contextlib import asynccontextmanager
from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import Base
from app.db_connection import get_engine, get_db_session
from app.operations import (
    create_ticket,
    get_ticket,
    update_ticket_price,
    delete_ticket,
    update_ticket_details,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/ticket/{ticket_id}")
async def read_ticket(
    ticket_id: int, db_session: Annotated[AsyncSession, Depends(get_db_session)]
):
    ticket = await get_ticket(db_session, ticket_id)

    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


class TicketRequest(BaseModel):
    price: float | None
    show: str | None
    user: str | None


@app.post("/ticket", response_model=dict[str, int])
async def create_ticket_route(
    ticket: TicketRequest, db_session: Annotated[AsyncSession, Depends(get_db_session)]
):
    ticket_id = await create_ticket(db_session, ticket.show, ticket.user, ticket.price)

    return {"ticket_id": ticket_id}


class TicketDetailsUpdateRequest(BaseModel):
    seat: str | None = None
    ticket_type: str | None = None


@app.put("/ticket/{ticket_id}/details")
async def update_ticket_route(
    ticket_id: int,
    ticket_details_update: TicketDetailsUpdateRequest,
    db_session: Annotated[AsyncSession, Depends(get_db_session)],
):
    update_dict_args = ticket_details_update.model_dump(exclude_unset=True)
    updated = await update_ticket_details(db_session, ticket_id, update_dict_args)

    if not updated:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {"detail": "Ticket updated"}


@app.put("/ticket/{ticket_id}/price/{new_price}")
async def update_ticket_price_route(
    ticket_id: int,
    new_price: int,
    db_session: Annotated[AsyncSession, Depends(get_db_session)],
):
    updated = await update_ticket_price(db_session, ticket_id, new_price)

    if not updated:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {"detail": "Price updated"}


@app.delete("/ticket/{ticket_id}")
async def delete_ticket_route(
    ticket_id: int, db_session: Annotated[AsyncSession, Depends(get_db_session)]
):
    deleted = await delete_ticket(db_session, ticket_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {"detail": "Ticket removed"}

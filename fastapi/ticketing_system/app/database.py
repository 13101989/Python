from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int | None] = mapped_column(ForeignKey("events.id"))

    price: Mapped[float] = mapped_column(nullable=True)
    show: Mapped[str | None]
    user: Mapped[str | None]
    sold: Mapped[bool] = mapped_column(default=False, server_default="false")

    details: Mapped["TicketDetails"] = relationship(back_populates="ticket")
    event: Mapped["Event | None"] = relationship(back_populates="tickets")


class TicketDetails(Base):
    __tablename__ = "ticket_details"

    id: Mapped[int] = mapped_column(primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id"))

    seat: Mapped[str | None]
    ticket_type: Mapped[str | None]

    ticket: Mapped["Ticket"] = relationship(back_populates="details")


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="event")

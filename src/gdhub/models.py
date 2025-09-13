import datetime
import decimal

from sqlalchemy import Date, DateTime, ForeignKey, Index, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from gdhub.db import Base

# Remove the old Base definition if present
# Base = declarative_base()


class Inmate(Base):
    __tablename__ = "inmates"
    id: Mapped[int] = mapped_column(primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(64), unique=True)
    first_name: Mapped[str | None] = mapped_column(String(64))
    last_name: Mapped[str | None] = mapped_column(String(64))
    dob: Mapped[datetime.date | None] = mapped_column(Date)
    sex: Mapped[str | None] = mapped_column(String(16))
    race: Mapped[str | None] = mapped_column(String(32))
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
    bookings: Mapped[list["Booking"]] = relationship(
        back_populates="inmate", cascade="all,delete-orphan"
    )


Index("ix_inmates_name", Inmate.last_name, Inmate.first_name)
Index("ix_inmates_external", Inmate.external_id)


class Booking(Base):
    __tablename__ = "bookings"
    id: Mapped[int] = mapped_column(primary_key=True)
    inmate_id: Mapped[int] = mapped_column(
        ForeignKey("inmates.id", ondelete="CASCADE"), index=True
    )
    booking_number: Mapped[str | None] = mapped_column(String(64), unique=True)
    booking_datetime: Mapped[datetime.datetime | None] = mapped_column(DateTime)
    release_datetime: Mapped[datetime.datetime | None] = mapped_column(DateTime)
    facility: Mapped[str | None] = mapped_column(String(128))
    status: Mapped[str | None] = mapped_column(String(32))
    source_url: Mapped[str | None] = mapped_column(String(512))
    raw_hash: Mapped[str | None] = mapped_column(String(64), index=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
    inmate: Mapped["Inmate"] = relationship(back_populates="bookings")
    charges: Mapped[list["Charge"]] = relationship(
        back_populates="booking", cascade="all,delete-orphan"
    )


Index("ix_bookings_inmate_time", Booking.inmate_id, Booking.booking_datetime.desc())


class Charge(Base):
    __tablename__ = "charges"
    id: Mapped[int] = mapped_column(primary_key=True)
    booking_id: Mapped[int] = mapped_column(
        ForeignKey("bookings.id", ondelete="CASCADE"), index=True
    )
    statute: Mapped[str | None] = mapped_column(String(64), index=True)
    description: Mapped[str | None] = mapped_column(String(256))
    severity: Mapped[str | None] = mapped_column(String(32))
    bond_amount: Mapped[decimal.Decimal | None] = mapped_column(Numeric)
    bond_type: Mapped[str | None] = mapped_column(String(32))
    disposition: Mapped[str | None] = mapped_column(String(64))
    court_date: Mapped[datetime.date | None] = mapped_column(Date)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
    booking: Mapped["Booking"] = relationship(back_populates="charges")


class Snapshot(Base):
    __tablename__ = "snapshots"
    id: Mapped[int] = mapped_column(primary_key=True)
    snapshot_date: Mapped[datetime.date] = mapped_column(Date, index=True)
    inmate_id: Mapped[int | None] = mapped_column(index=True)
    booking_id: Mapped[int | None] = mapped_column(index=True)
    charge_id: Mapped[int | None] = mapped_column(index=True)

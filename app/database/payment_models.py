from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.models import Base


class Payment(Base):
    """
    Платеж ProfitOS
    """

    __tablename__ = "payments"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )


    amount: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    currency: Mapped[str] = mapped_column(
        String(10),
        default="RUB"
    )


    payment_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )


    is_paid: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
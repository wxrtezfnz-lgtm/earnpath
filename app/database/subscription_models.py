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


class Subscription(Base):
    """
    Подписка пользователя ProfitOS
    """

    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    plan: Mapped[str] = mapped_column(
        String(50),
        default="premium"
    )

    payment_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
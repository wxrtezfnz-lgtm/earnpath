from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Integer,
    String
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)



class Base(DeclarativeBase):
    pass



class User(Base):

    __tablename__ = "users"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        index=True
    )


    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    first_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    level: Mapped[int] = mapped_column(
        Integer,
        default=1
    )


    xp: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    design_progress: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    is_premium: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
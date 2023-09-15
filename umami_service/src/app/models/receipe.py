

from sqlalchemy.orm import Mapped, mapped_column

from app.config.db import Base


class ReceipeModel(Base):
    """Модель рецепта."""

    __tablename__ = "receipe"

    receipe_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

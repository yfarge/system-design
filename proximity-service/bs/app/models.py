from sqlalchemy import Double
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.db import Model


class Business(Model):
    business_id: Mapped[int] = mapped_column(primary_key=True)
    latitude: Mapped[float] = mapped_column(
        Double(120), index=True, unique=True)
    longtitude: Mapped[float] = mapped_column(
        Double(120), index=True, unique=True)

    def __repr__(self) -> str:
        return '<Business {}>'.format(self.business_id)

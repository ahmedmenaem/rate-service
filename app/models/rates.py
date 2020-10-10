from sqlalchemy import Column, String, Float, Integer, Date
from app.db.base_class import Base
from app.db.session import engine


class Rate(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    base_currency = Column(String(3), nullable=False)
    target_currency = Column(String(3), nullable=False)
    rate = Column(Float, nullable=False)
    exchange_date = Column(Date, nullable=False)


Base.metadata.create_all(engine)

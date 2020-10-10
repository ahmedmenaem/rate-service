from pydantic import BaseModel
from datetime import date


class Rate(BaseModel):
    id: int
    exchangeDate: date
    rate: float
    baseCurrency: str
    targetCurrency: str

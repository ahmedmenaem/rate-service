from fastapi import APIRouter, Query
from typing import Optional, Any
from datetime import date
from app.controllers.rates import get_rate
from app.schemas.rate import Rate
from app.models.currency import Currency

router = APIRouter()


@router.get('', response_model=Rate)
async def get_rate_controller(
    base_currency: Currency,
    target_currency: Currency,
    exchange_date: Optional[date] = Query(date.today())
):
    print(base_currency, target_currency, exchange_date)
    rate = await get_rate(base_currency, target_currency, exchange_date)
    return rate

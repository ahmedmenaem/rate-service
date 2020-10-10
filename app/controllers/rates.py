from typing import Any
from datetime import date
from app.api.rates import get_exchange_rate
from app.models.rates import Rate
from sqlalchemy import func
from app.utils.deps import get_db


async def get_rate(base_currency: str = None, target_currency: str = None, exchange_date: date = date.today()) -> Any:
    try:
        db = get_db()
        rate = None
        saved_rate = db.query(Rate).filter(func.date(Rate.exchange_date) == exchange_date).filter(
            Rate.base_currency == base_currency).filter(Rate.target_currency == target_currency).first()
        if saved_rate:
            rate = saved_rate
        else:
            external_rate = get_exchange_rate(
                base_currency, target_currency, exchange_date)
            rate = Rate(base_currency=base_currency, target_currency=target_currency,
                        exchange_date=exchange_date, rate=external_rate['rates'][target_currency])
            db.add(rate)
            db.commit()
        return {
            'id': rate.id,
            'exchangeDate': rate.exchange_date,
            'baseCurrency': base_currency,
            'targetCurrency': target_currency,
            'rate': rate.rate
        }
    except:
        db.rollback()

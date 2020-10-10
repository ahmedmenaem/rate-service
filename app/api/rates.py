from requests import get
from app.core.config import settings
from datetime import date
from typing import Any


def get_exchange_rate(base_currency: str, target_currency: str, exchange_date: date) -> Any:
    endpoint = f'{settings.RATES_API_HOST}{exchange_date}?from={base_currency}&to={target_currency}'
    response = get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

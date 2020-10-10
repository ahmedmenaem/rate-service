import os
from pydantic import BaseSettings, PostgresDsn, validator, AnyHttpUrl, HttpUrl
from typing import Any, Dict, Optional


class Settings(BaseSettings):
    SERVER_PORT: int = int(os.getenv('SERVER_PORT', 8080))
    SERVER_HOST: str = os.getenv('SERVER_HOST', '0.0.0.0')

    # postres confifs
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST', '0.0.0.0')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'admin')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'admin@@1234')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'rates_db')
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # Rates third-party configs
    RATES_API_HOST: HttpUrl = os.getenv(
        'RATES_API_HOST', 'https://www.frankfurter.app/')

    class Config:
        case_sensitive = True


settings = Settings()

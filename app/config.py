from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://bitcoin:123456@localhost:5432/bitcoin"
    tron_network_url: str = "https://apilist.tronscanapi.com/api/account?address="
    page_size: int = 10

    class Config:
        env_file = ".env"

settings = Settings()
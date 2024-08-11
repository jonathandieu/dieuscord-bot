from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=(".env", ".env.local", ".env.prod"),
        env_file_encoding="utf-8",
    )
    ENVIRONMENT: str
    BOT_TOKEN: str


settings = Settings()
print("Settings loaded")
print(f"Environment: {settings.ENVIRONMENT=}")

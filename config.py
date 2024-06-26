from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    slack_webhook: str

    reddit_client_id: str
    reddit_client_secret: str
    reddit_username: str
    reddit_password: str
    reddit_user_agent: str = "redditin"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


def get_settings():
    return Settings()


settings = get_settings()

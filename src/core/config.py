from pydantic import PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

#  [ ]  configurar o banco de dados
#  [ ]  configurar o rota  padrão 'api/vi'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env")
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_SERVER: str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=5432,
        )


settings = Settings()


print(settings.SQLALCHEMY_DATABASE_URI)

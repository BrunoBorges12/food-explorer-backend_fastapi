from pydantic_settings import BaseSettings, SettingsConfigDict

#  [ ]  configurar o banco de dados
#  [ ]  configurar o rota  padrão 'api/vi'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env")
    TESTE_API: str


settings = Settings()

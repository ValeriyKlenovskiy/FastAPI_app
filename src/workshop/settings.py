from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./database.sqlite3'

    jwt_secret: str = '2uO7qP-F33HyK0lcAFB9ZlQ3jlrizhQbrguE_YN_l-E'
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)


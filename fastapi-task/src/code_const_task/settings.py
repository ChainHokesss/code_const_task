from pydantic import BaseSettings

class Settings(BaseSettings):
    port: int = 8000
    host: str = '127.0.0.1'
    reload: bool = True
    database_url: str = 'sqlite:////Users/nazarkurilovic/Desktop/MAIN/code_const_task/database.sqlite3'
    jwt_secret: str = 'MY_SECRET_KEY'
    jwt_algorithm: str = 'HS256'
    jwt_expires_s: int = 3600

settings = Settings()
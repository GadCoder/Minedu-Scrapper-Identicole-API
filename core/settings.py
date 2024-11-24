import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

class Settings:
    MYSQL_USER: str = os.getenv("user")
    MYSQL_HOST: str = os.getenv("host")
    MYSQL_PASSWORD: str = os.getenv("password")
    MYSQL_DATABASE: str = os.getenv("database")

    DATABASE_URL: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DATABASE}"


settings = Settings()
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

class Config:
    DB_NAME = os.getenv("DB_NAME", "users.db")
    
    API_TITLE = "用户管理系统"
    API_VERSION = "1.0.0"
    
config = Config()
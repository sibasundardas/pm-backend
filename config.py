import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey123")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "myjwtsecret123")
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

    # --- FINAL CONNECTION LOGIC ---
    # This reads the single database URL variable from Railway.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # --- END FINAL LOGIC ---

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

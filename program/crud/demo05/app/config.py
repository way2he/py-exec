# app/config.py
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///../../../sqlite/mySqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET', 'default-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1小时
    RATELIMIT_DEFAULT = "200 per day"
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

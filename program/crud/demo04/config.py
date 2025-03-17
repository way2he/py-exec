import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '../../../sqlite/mySqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用修改追踪‌

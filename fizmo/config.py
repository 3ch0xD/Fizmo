import os
from flask import current_app

class Config:
    DB_NAME = "databse.db"
    SECRET_KEY = "1Lion:raWr@A}p"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"

import os

class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/taskdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "your_jwt_secret"
    CELERY_BROKER_URL = "redis://localhost:6379/0"
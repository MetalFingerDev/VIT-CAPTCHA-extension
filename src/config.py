# config.py


import os

class BaseConfig:
    DEBUG = False
    PORT = int(os.getenv("PORT", 8008))
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ALLOWED_ORIGINS = [
        r"http://localhost:\d+",
        r"http://127\.0\.0\.1:\d+"
    ]

class ProductionConfig(BaseConfig):
    ALLOWED_ORIGINS = [
        "https://yourdomain.com",
        "https://api.yourdomain.com"
    ]

def get_config():
    env = os.getenv("FLASK_ENV", "production")
    return ProductionConfig if env == "production" else DevelopmentConfig

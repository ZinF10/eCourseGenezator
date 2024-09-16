import os, secrets
from dotenv import load_dotenv

load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(32))
    DEBUG = False
    FLASK_ADMIN_SWATCH = 'lux'
    PAGE_SIZE = 10


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'database', 'ecourse.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'database', 'ecourse_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
)
import os


def Config:
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///:memory:")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


def ProductionConfig(Config):
    DEBUG = False
    TESTING = False


def StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


def DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


def TestConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

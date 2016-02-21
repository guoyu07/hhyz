# encoding=utf-8
import os
path=os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    HHYZ_MAIL_SUBJECT_PREFIX = '[Flasky]'
    HHYZ_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    HHYZ_ADMIN = os.environ.get('FLASKY_ADMIN')
    HHYZ_POSTS_PER_PAGE = 15
    HHYZ_COMMENTS_PER_PAGE =20
    HHYZ_SLOW_DB_QUERY_TIME=0.5

    @staticmethod
    def init_app(app):
        pass

class DefaultConfig(Config):
    # DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(path, 'data-dev.sqlite')
    SQLALCHEMY_DATABASE_URI='mysql://root:@127.0.0.1:3306/hhyz'
class TestConfig(Config):
    pass

class ProductionConfig(Config):
    pass

config={
    'default':DefaultConfig,
    'test':TestConfig,
    'product':ProductionConfig,
}
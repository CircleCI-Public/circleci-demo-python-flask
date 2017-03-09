import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # run mailhog for development emails
    MAIL_SERVER = os.environ.get('SERVER') or 'localhost'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 1025
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'mailhog'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'mailhog'
    CIRCULATE_MAIL_SUBJECT_PREFIX = '[Circulate]'
    CIRCULATE_MAIL_SENDER = os.environ.get('CIRCULATE_MAIL_SENDER') or \
        'Circulate Admin <circulate@example.com>'
    CIRCULATE_ADMIN = os.environ.get('CIRCULATE_ADMIN') or 'circulate@example.com'
    CIRCULATE_POSTS_PER_PAGE = 20
    CIRCULATE_FOLLOWERS_PER_PAGE = 50
    CIRCULATE_COMMENTS_PER_PAGE = 30
    CIRCULATE_SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://localhost/circulate'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'postgresql://localhost/circulate'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://localhost/circulate'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.CIRCULATE_MAIL_SENDER,
            toaddrs=[cls.CIRCULATE_ADMIN],
            subject=cls.CIRCULATE_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


class HerokuConfig(ProductionConfig):
    SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'unix': UnixConfig,

    'default': DevelopmentConfig
}

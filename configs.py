class Configuration(object):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql://testuser:123456@localhost:5432/postgrestest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'placeholder'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
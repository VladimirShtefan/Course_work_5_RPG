class BaseConfig:
    JSON_AS_ASCII = False
    TESTING = False
    DEBUG = False


class DevConfig(BaseConfig):
    TESTING = True
    DEBUG = True


class ProdConfig(BaseConfig):
    pass

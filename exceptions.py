class BaseAppException(Exception):
    code = 500


class NotFound(BaseAppException):
    code = 404


class BadRequest(BaseAppException):
    code = 400


class DataError(BaseAppException):
    message = 'Ресурс временно недоступен'
    code = 503

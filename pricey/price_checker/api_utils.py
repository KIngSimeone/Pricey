from rest_framework.response import Response
from enum import IntEnum

class ErrorCodes(IntEnum):
    GENERIC_ERROR = 0
    UNAUTHENTICATED = 1
    UNAUTHORIZED = 2
    FORBIDDEN = 3

    MISSING_HEADER = 4
    MISSING_FIELDS = 5
    INVALID_PAYLOAD = 6
    INVALID_FIELD = 7
    INVALID_FORMAT = 8
    INVALID_TYPE = 9
    INVALID_CREDENTIALS = 10

    UPDATE_FAILED = 11
    CREATE_FAILED = 12
    ALREADY_EXISTS = 13
    UPLOAD_FAILED = 14
    CONNECTION_FAILED = 15
    APPROVED_FAILED = 16
    DELETE_FAILED = 17

    CONFLICT = 18
    LIMIT_REACHED = 19
    NOT_FOUND = 20

    TIMEOUT = 21
    SERVER_ERROR = 22
    SERVICE_UNAVAILABLE = 23



def http_response(msg, status, data=None, error_code=None):

    if data is None:
        data = {}
    success = True
    responseData = dict(
        success=success,
        message=msg,
        data=data,
    )
    if error_code:
        success = False
        responseData['success'] = success
        responseData['error_code'] = error_code

    return Response(responseData, status=status)
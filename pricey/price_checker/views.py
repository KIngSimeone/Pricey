import requests
import logging
from rest_framework.decorators import api_view
from .api_utils import http_response, ErrorCodes
from rest_framework import status

# Get an instance of a logger
logger = logging.getLogger(__name__)

@api_view(['GET'])
def price_validator(request):

    isValid = True if validate_password_resettoken(token) else False
    if not isValid:
        return http_response(
            msg="Invalid Reset Token",
            status=status.HTTP_400_BAD_REQUEST,
            error_code=ErrorCodes.INVALID_FIELD,
        )

    return http_response(
        msg="Token is valid",
        status=status.HTTP_200_OK,
        data={"isValid": isValid}
    )
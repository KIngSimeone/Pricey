import requests
import logging
from rest_framework.decorators import api_view
from .api_utils import http_response, ErrorCodes
from rest_framework import status

# Get an instance of a logger
logger = logging.getLogger(__name__)

@api_view(['GET'])
def price_validator(request):
    url = "https://dev.oxinar.uk/test/api/item"
    headers = {
        'Content-Type': 'application/json',
    }
    price_request = requests.get(url, headers=headers)
    price_response = price_request.json()
    print(price_response)

    return http_response(
        msg="success",
        status=status.HTTP_200_OK,
        data=price_response
    )
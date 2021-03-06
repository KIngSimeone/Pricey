import logging

import requests
from rest_framework import status
from rest_framework.decorators import api_view

from .api_utils import ErrorCodes, http_response
from .utils import create_price_record

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
    max_price = price_response['max_price']
    price = price_response['price']
    if price < max_price:
        create_price_record(price, max_price)
        msg = "Price is less than the Max Price, hense result logged"
    else:
        msg = "Price is greated thean the Max price"

    return http_response(
        msg=msg,
        status=status.HTTP_200_OK,
        data=price_response
    )

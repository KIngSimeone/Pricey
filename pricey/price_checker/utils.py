from .models import Prices
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def create_price_record(price, max_price):
    try:
        price_record = Prices.objects.create(
            price=price,
            max_price=max_price,
        )

        return price_record

    except Exception as e:
        logger.error(
            "create_price_record@Error")
        logger.error(e)
        return None
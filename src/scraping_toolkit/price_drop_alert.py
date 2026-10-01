"""Alert system for price drops."""

import logging
from typing import Optional

from .config import config
from .http_client import HTTPClient

logger = logging.getLogger(__name__)


class PriceDropAlert:
    """Monitors a specific product and sends an alert if the price drops."""

    def __init__(self, client: Optional[HTTPClient] = None) -> None:
        """Initialize the alert system."""
        self.client = client or HTTPClient()

    def check_price_drop(
        self,
        target_url: str,
        old_price: float,
        current_price_mock: Optional[float] = None,
    ) -> bool:
        """
        Check if the price has dropped below the old price.
        Note: current_price_mock is used here to mimic the original script's behavior
        without scraping a real unavailable/example.com page.

        Args:
            target_url: URL of the product.
            old_price: The baseline price to compare against.
            current_price_mock: A mock price for demonstration.

        Returns:
            True if price dropped, False otherwise.
        """
        logger.info(f"Checking price drop for {target_url}")

        # In a real scenario, we would scrape the current price here:
        # response = self.client.get(target_url)
        # current_price = parse_price(response.text)

        # Using mock behavior from the original script
        current_price = (
            current_price_mock if current_price_mock is not None else 55000.0
        )

        logger.debug(f"Old price: {old_price}, Current price: {current_price}")

        if current_price < old_price:
            logger.info("Price dropped!")
            self._send_alert()
            return True
        else:
            logger.info("Price not dropped.")
            return False

    def _send_alert(self) -> None:
        """Send an email alert."""
        email = config.EMAIL_SENDER or "client@gmail.com"
        logger.info(f"Sending price drop alert to {email}")
        # Email sending logic would go here

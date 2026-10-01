"""Scraper for tracking book prices and saving history."""

import logging
from typing import Dict, List

from .book_scraper import BookScraper
from .utils import export_to_json

logger = logging.getLogger(__name__)


class PriceTracker:
    """Tracks prices and exports them to a JSON file."""

    def __init__(self, scraper: BookScraper = None) -> None:
        """Initialize the tracker."""
        self.scraper = scraper or BookScraper()

    def track_and_save(self, output_file: str = "price_history.json") -> bool:
        """
        Scrape current prices and save them to a file.

        Args:
            output_file: The destination JSON file path.

        Returns:
            True if successful, False otherwise.
        """
        logger.info("Starting price tracking run.")
        data: List[Dict[str, str]] = self.scraper.scrape_books()

        if not data:
            logger.error("No data scraped. Aborting save.")
            return False

        return export_to_json(data, output_file)

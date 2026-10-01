"""Scraper for extracting book titles and prices."""

import logging
from typing import Dict, List, Optional

from bs4 import BeautifulSoup

from .http_client import HTTPClient

logger = logging.getLogger(__name__)


class BookScraper:
    """Scrapes book information from books.toscrape.com."""

    BASE_URL = "https://books.toscrape.com"

    def __init__(self, client: Optional[HTTPClient] = None) -> None:
        """Initialize the scraper with an HTTP client."""
        self.client = client or HTTPClient()

    def scrape_books(self) -> List[Dict[str, str]]:
        """
        Scrape books from the main page.

        Returns:
            A list of dictionaries containing book titles and prices.
        """
        logger.info(f"Starting book scrape at {self.BASE_URL}")
        response = self.client.get(self.BASE_URL)

        if not response:
            logger.warning("Failed to fetch the main page. Returning empty list.")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        results = []
        for book in books:
            try:
                title = book.find("h3").find("a")["title"]
                price = book.find("p", class_="price_color").text
                results.append({"title": title, "price": price})
            except AttributeError as e:
                logger.error(f"Failed to parse a book item: {e}")

        logger.info(f"Successfully scraped {len(results)} books.")
        return results

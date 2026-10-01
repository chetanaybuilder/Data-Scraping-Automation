"""Tests for the scraping toolkit."""

from unittest.mock import MagicMock

import pytest

from src.scraping_toolkit.book_scraper import BookScraper
from src.scraping_toolkit.http_client import HTTPClient
from src.scraping_toolkit.price_drop_alert import PriceDropAlert


@pytest.fixture
def mock_http_client():
    """Provides a mocked HTTP client."""
    client = MagicMock(spec=HTTPClient)
    return client


def test_book_scraper_success(mock_http_client):
    """Test book scraping with a mocked successful HTML response."""
    mock_response = MagicMock()
    mock_response.text = """
    <html>
        <body>
            <article class="product_pod">
                <h3><a title="A Light in the Attic">A Light in the Attic</a></h3>
                <div class="product_price">
                    <p class="price_color">£51.77</p>
                </div>
            </article>
        </body>
    </html>
    """
    mock_http_client.get.return_value = mock_response

    scraper = BookScraper(client=mock_http_client)
    books = scraper.scrape_books()

    assert len(books) == 1
    assert books[0]["title"] == "A Light in the Attic"
    assert books[0]["price"] == "£51.77"


def test_book_scraper_failure(mock_http_client):
    """Test book scraping when HTTP request fails."""
    mock_http_client.get.return_value = None

    scraper = BookScraper(client=mock_http_client)
    books = scraper.scrape_books()

    assert len(books) == 0


def test_price_drop_alert():
    """Test the price drop logic."""
    alert = PriceDropAlert()

    # Should alert if current (55000) < old (60000)
    assert (
        alert.check_price_drop("http://test.com", 60000.0, current_price_mock=55000.0)
        is True
    )

    # Should not alert if current (65000) >= old (60000)
    assert (
        alert.check_price_drop("http://test.com", 60000.0, current_price_mock=65000.0)
        is False
    )

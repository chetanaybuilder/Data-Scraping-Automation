"""Command-line interface for the scraping toolkit."""

import argparse
import logging

from dotenv import load_dotenv

from src.scraping_toolkit.book_scraper import BookScraper
from src.scraping_toolkit.price_drop_alert import PriceDropAlert
from src.scraping_toolkit.price_tracker import PriceTracker
from src.scraping_toolkit.utils import setup_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the CLI application."""
    load_dotenv()
    setup_logging()

    parser = argparse.ArgumentParser(description="Professional Scraping Toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Book scraper command
    subparsers.add_parser("books", help="Scrape book titles and prices")

    # Price tracker command
    track_parser = subparsers.add_parser("track", help="Track prices and save to JSON")
    track_parser.add_argument(
        "--output", default="price_history.json", help="Output file path"
    )

    # Price alert command
    alert_parser = subparsers.add_parser("alert", help="Check for price drops")
    alert_parser.add_argument(
        "--url", default="https://example.com/product", help="Target URL"
    )
    alert_parser.add_argument(
        "--old-price", type=float, default=60000, help="Previous price"
    )

    args = parser.parse_args()

    if args.command == "books":
        scraper = BookScraper()
        books = scraper.scrape_books()
        for book in books:
            print(f"{book['title']} - {book['price']}")

    elif args.command == "track":
        tracker = PriceTracker()
        tracker.track_and_save(args.output)

    elif args.command == "alert":
        alert = PriceDropAlert()
        alert.check_price_drop(args.url, args.old_price, current_price_mock=55000.0)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

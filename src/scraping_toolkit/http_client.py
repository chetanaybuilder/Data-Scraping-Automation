"""Robust HTTP client with retries and timeouts."""

import logging
import time
from typing import Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import config

logger = logging.getLogger(__name__)


class HTTPClient:
    """A resilient HTTP client for web scraping."""

    def __init__(self) -> None:
        """Initialize the HTTP session with retry logic and standard headers."""
        self.session = requests.Session()

        # Configure retries
        retry_strategy = Retry(
            total=config.MAX_RETRIES,
            backoff_factor=config.RETRY_BACKOFF_FACTOR,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Set default headers
        self.session.headers.update({"User-Agent": config.USER_AGENT})

    def get(self, url: str, delay: bool = True) -> Optional[requests.Response]:
        """
        Send a GET request to the specified URL.

        Args:
            url: The target URL.
            delay: Whether to add a polite delay before requesting.

        Returns:
            The HTTP response, or None if the request failed.
        """
        if delay:
            logger.debug(f"Sleeping for {config.REQUEST_DELAY}s before request...")
            time.sleep(config.REQUEST_DELAY)

        try:
            logger.info(f"Fetching URL: {url}")
            response = self.session.get(url, timeout=config.DEFAULT_TIMEOUT)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error occurred: {e}")
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout error occurred: {e}")
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred: {e}")

        return None

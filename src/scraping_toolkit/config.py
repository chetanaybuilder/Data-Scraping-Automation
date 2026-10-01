"""Configuration settings and environment loading."""

import os
from typing import Optional


class Config:
    """Application configuration management."""

    # Default settings
    DEFAULT_TIMEOUT: int = int(os.getenv("SCRAPER_TIMEOUT", "10"))
    MAX_RETRIES: int = int(os.getenv("SCRAPER_MAX_RETRIES", "3"))
    RETRY_BACKOFF_FACTOR: float = float(os.getenv("SCRAPER_BACKOFF_FACTOR", "0.3"))

    # Delay between requests (respecting robots)
    REQUEST_DELAY: float = float(os.getenv("SCRAPER_REQUEST_DELAY", "2.0"))

    # User agent for requests
    USER_AGENT: str = os.getenv(
        "SCRAPER_USER_AGENT",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    )

    # API Keys / Sensitive info (loaded from .env)
    EMAIL_SENDER: Optional[str] = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD: Optional[str] = os.getenv("EMAIL_PASSWORD")


config = Config()

"""Utility functions for logging and data export."""

import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List


def setup_logging(level: int = logging.INFO) -> None:
    """Configure application logging."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def export_to_json(data: List[Dict[str, Any]], filepath: str) -> bool:
    """
    Export scraped data to a JSON file.

    Args:
        data: A list of dictionaries containing the scraped data.
        filepath: The destination file path.

    Returns:
        True if successful, False otherwise.
    """
    logger = logging.getLogger(__name__)
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        logger.info(f"Successfully exported data to {filepath}")
        return True
    except Exception as e:
        logger.error(f"Failed to export data to {filepath}: {e}")
        return False

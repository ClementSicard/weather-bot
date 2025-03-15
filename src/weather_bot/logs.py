"""Logging setup for the weather bot."""

from pathlib import Path

from loguru import logger


DEFAULT_LOG_FLDER = Path("logs")


def setup_logs() -> None:
    """Set up logging."""
    DEFAULT_LOG_FLDER.mkdir(exist_ok=True)
    logger.add(DEFAULT_LOG_FLDER / "weather_bot.log")
    logger.info("Logging initialized.")

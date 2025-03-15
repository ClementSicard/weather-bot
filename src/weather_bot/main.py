"""Entrypoint."""

import argparse
import os
import random

from loguru import logger

from weather_bot.data.meteoswiss import MeteoSwiss
from weather_bot.logs import setup_logs
from weather_bot.telegram.bot import TelegramBot
from weather_bot.telegram.env import Env
from weather_bot.telegram.message import API_ERROR_MESSAGE
from weather_bot.telegram.message import MESSAGES

from typing import Any


def main(args: dict[str, Any]) -> None:
    """Main entry point for the application script."""
    env = Env()
    bot = TelegramBot(bot_token=env.bot_token, chat_id=env.chat_id)

    try:
        meteoswiss = MeteoSwiss()
        if meteoswiss.is_raining_today(zip_code=args["zip_code"]):
            message = random.choice(MESSAGES)  # noqa: S311
            bot.send_telegram_message(message.format(args["zip_code"]))
            logger.warning("⚠️ Rain today! ⛈️")
        else:
            logger.info("No rain today! 🌞 See you tomorrow")

    except LookupError as e:
        logger.error("Failed to query Meteoswiss API.")
        bot.send_telegram_message(API_ERROR_MESSAGE.format(repr(e)))
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        bot.send_telegram_message(API_ERROR_MESSAGE.format(repr(e)))


if __name__ == "__main__":
    setup_logs()
    parser = argparse.ArgumentParser(description="Weather bot")
    parser.add_argument(
        "--zip_code",
        type=int,
        help="Zip code for the location",
        default=os.environ.get("ZIP_CODE"),
    )
    args = parser.parse_args()
    main(args=vars(args))

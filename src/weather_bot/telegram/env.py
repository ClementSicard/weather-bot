"""Module for storing environment variables for the bot."""

import os

from dotenv import load_dotenv


class Env:
    """Class storing all the environment variables for the bot."""

    def __init__(self):
        """Constructor."""
        load_dotenv()

    @property
    def bot_token(self) -> str:
        """Returns the bot token."""
        token = os.getenv('TELEGRAM_BOT_TOKEN')
        if token is None:
            raise ValueError('API key not found in environment variables.')
        return token

    @property
    def chat_id(self) -> str:
        """Returns the chat ID."""
        token = os.getenv('TELEGRAM_CHAT_ID')
        if token is None:
            raise ValueError('API key not found in environment variables.')
        return token

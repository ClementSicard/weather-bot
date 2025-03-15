"""Module for sending messages to Telegram group/private conversation."""

from loguru import logger
import requests


class TelegramBot:
    """Class for sending messages to Telegram."""

    DEFAULT_TIMEOUT = 10  # 10 seconds

    def __init__(
        self, bot_token: str, chat_id: str, timeout: int = DEFAULT_TIMEOUT
    ) -> None:
        """Constructor."""
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.timeout = timeout

    def send_telegram_message(self, message: str) -> None:
        """Send a message to a Telegram chat.

        Args:
            message (str): The message to send.
        """
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message}
        response = requests.post(url, json=payload, timeout=self.timeout)

        logger.info(url)
        logger.info(payload)
        logger.warning(response.json())

        if response.status_code == requests.codes["ok"]:
            logger.success(f"Message sent successfully to chat {self.chat_id}!")
        else:
            logger.error("Failed to send message:", response.text)

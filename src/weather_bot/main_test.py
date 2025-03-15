"""Tests for the main function."""

from unittest import mock

from weather_bot.main import main


@mock.patch("weather_bot.main.MeteoSwiss.is_raining_today", side_effect=True)
@mock.patch("weather_bot.main.TelegramBot.send_telegram_message")
def test_e2e(
    mocked_telegram_bot: mock.Mock,
    mocked_meteoswiss_call: mock.Mock,
) -> None:
    """Test that the main function does not raise an AssertionError."""
    main({"zip_code": 1018})

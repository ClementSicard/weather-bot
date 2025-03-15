"""Tests for the main function."""

from unittest import mock

from weather_bot.main import main


SAMPLE_RESPONSE = {
    "plz": 101800,
    "currentWeather": {
        "time": 1741471200000,
        "icon": 101,
        "iconV2": 101,
        "temperature": 8.6,
    },
    "regionForecast": [
        {
            "dayDate": "2025-03-08",
            "iconDay": 2,
            "iconDayV2": 2,
            "temperatureMax": 15,
            "temperatureMin": 5,
            "precipitation": 0.0,
            "precipitationMin": 0.0,
            "precipitationMax": 0.0,
        },
        {
            "dayDate": "2025-03-09",
            "iconDay": 26,
            "iconDayV2": 26,
            "temperatureMax": 15,
            "temperatureMin": 6,
            "precipitation": 0.0,
            "precipitationMin": 0.0,
            "precipitationMax": 0.0,
        },
        {
            "dayDate": "2025-03-10",
            "iconDay": 32,
            "iconDayV2": 32,
            "temperatureMax": 12,
            "temperatureMin": 7,
            "precipitation": 3.5,
            "precipitationMin": 0.5,
            "precipitationMax": 9.0,
        },
        {
            "dayDate": "2025-03-11",
            "iconDay": 3,
            "iconDayV2": 3,
            "temperatureMax": 11,
            "temperatureMin": 5,
            "precipitation": 0.5,
            "precipitationMin": 0.0,
            "precipitationMax": 4.6,
        },
        {
            "dayDate": "2025-03-12",
            "iconDay": 17,
            "iconDayV2": 17,
            "temperatureMax": 10,
            "temperatureMin": 5,
            "precipitation": 2.6,
            "precipitationMin": 0.0,
            "precipitationMax": 10.5,
        },
        {
            "dayDate": "2025-03-13",
            "iconDay": 5,
            "iconDayV2": 5,
            "temperatureMax": 9,
            "temperatureMin": 4,
            "precipitation": 0.6,
            "precipitationMin": 0.0,
            "precipitationMax": 6.5,
        },
    ],
}


@mock.patch(
    "weather_bot.main.MeteoSwiss.query_forecast", side_effect=SAMPLE_RESPONSE
)
@mock.patch("weather_bot.main.TelegramBot.send_telegram_message")
@mock.patch("weather_bot.main.Env")
def test_e2e(
    mocked_env_loading: mock.Mock,
    mocked_telegram_bot: mock.Mock,
    mocked_meteoswiss_call: mock.Mock,
) -> None:
    """Test that the main function does not raise an AssertionError."""
    main({"zip_code": 1018})

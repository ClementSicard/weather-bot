"""MeteoSwiss tests."""

import pytest

from weather_bot.data.meteoswiss import MeteoSwiss

from typing import Any


@pytest.mark.parametrize(
    "day_data,expected",
    [
        (
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
            True,
        ),
        (
            {
                "dayDate": "2025-03-11",
                "iconDay": 3,
                "iconDayV2": 3,
                "temperatureMax": 11,
                "temperatureMin": 5,
                "precipitation": 0.0,
                "precipitationMin": 0.0,
                "precipitationMax": 4.6,
            },
            False,
        ),
    ],
)
def test_is_raining_on_day(day_data: dict[str, Any], expected: bool) -> None:
    """Test the is_raining_on_day method."""
    meteoswiss = MeteoSwiss()
    assert meteoswiss.is_raining_on_day(day_data) == expected

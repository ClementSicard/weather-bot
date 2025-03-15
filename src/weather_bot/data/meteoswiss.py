"""Meteoswiss API client."""

import requests
from tenacity import retry
from tenacity import stop_after_attempt

from typing import Any


class MeteoSwiss:
    """Meteoswiss API client.

    Only covers basic forecast query functionality.
    """

    BASE_URL = "https://app-prod-ws.meteoswiss-app.ch/v1/forecast"

    @retry(stop=stop_after_attempt(5))
    def query_forecast(self, zip_code: str) -> dict[str, Any]:
        """Query the Meteoswiss API for the forecast."""
        params = {"plz": zip_code}
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError("Failed to query Meteoswiss API.") from e

    def is_raining_on_day(self, day_data: dict[str, Any]) -> bool:
        """Check if it is raining on a specific day."""
        if "precipitation" not in day_data:
            raise LookupError(
                f"Precipitation data not found in JSON, only got {sorted(day_data.keys())}."
            )
        # return day_data["precipitation"] > 0.0
        return True

    def is_raining_today(self, zip_code: str) -> bool:
        """Check if it is raining today."""
        weekly_forecast = self.query_forecast(zip_code)
        today_forecast = weekly_forecast["regionForecast"][0]
        return self.is_raining_on_day(today_forecast)

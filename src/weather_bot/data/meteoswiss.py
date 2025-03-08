"""Meteoswiss API client."""

import requests

from typing import Any


class MeteoSwiss:
    """Meteoswiss API client.

    Only covers basic forecast query functionality.
    """

    BASE_URL = "https://app-prod-ws.meteoswiss-app.ch/v1/forecast"

    def query_forecast(self, zip_code: str) -> dict[str, Any]:
        """Query the Meteoswiss API for the forecast."""
        # Make the request and process the response
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
        return day_data["precipitation"] > 0.0

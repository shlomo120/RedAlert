from datetime import timedelta
import logging
import requests
from homeassistant.const import STATE_UNKNOWN
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

class RedAlertCurrentCitySensor(Entity):
    """Representation of the current city Red Alert sensor."""

    def __init__(self, resource, headers, verify_ssl, city, interval):
        """Initialize the sensor."""
        self._resource = resource
        self._headers = headers
        self._verify_ssl = verify_ssl
        self._city = city
        self._interval = interval
        self._state = False

        self.update_interval = timedelta(seconds=self._interval)

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Current City Red Alert"

    @property
    def state(self):
        """Return the state of the sensor (True if alarm is active in the chosen city, False otherwise)."""
        return self._state

    def update(self):
        """Fetch the data from the Red Alert API and check if the alarm is active in the chosen city."""
        try:
            response = requests.get(self._resource, headers=self._headers, verify=self._verify_ssl)
            response.raise_for_status()
            data = response.json()

            # Check if the alarm is active in the chosen city
            alerts_for_city = [alert for alert in data if self._city in alert["data"]]
            self._state = any(alert["cat"] == "1" for alert in alerts_for_city)
        except requests.exceptions.RequestException as error:
            _LOGGER.error("Error fetching data: %s", error)
            self._state = False

class RedAlertCountryWideSensor(Entity):
    """Representation of the country-wide Red Alert sensor."""

    def __init__(self, resource, headers, verify_ssl, interval):
        """Initialize the sensor."""
        self._resource = resource
        self._headers = headers
        self._verify_ssl = verify_ssl
        self._interval = interval
        self._state = []

        self.update_interval = timedelta(seconds=self._interval)

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Country-Wide Red Alert"

    @property
    def state(self):
        """Return a comma-separated string of city names with active alarms."""
        return ", ".join(self._state)

    def update(self):
        """Fetch the data from the Red Alert API and collect city names with active alarms."""
        try:
            response = requests.get(self._resource, headers=self._headers, verify=self._verify_ssl)
            response.raise_for_status()
            data = response.json()

            # Collect city names with active alarms
            self._state = [alert["data"] for alert in data if alert["cat"] == "1"]
        except requests.exceptions.RequestException as error:
            _LOGGER.error("Error fetching data: %s", error)
            self._state = []



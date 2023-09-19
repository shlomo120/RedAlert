import logging
from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN  # Replace with the actual name of your integration domain

_LOGGER = logging.getLogger(__name__)

# Define the configuration options for the city and interval (in seconds)
CONF_CITY = "city"
CONF_INTERVAL = "interval"

# Default values
DEFAULT_CITY = "תל אביב"
DEFAULT_INTERVAL = 15  # Default polling interval is 15 seconds

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Red Alert integration."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Validate and save the user's city and interval input here
            self._async_abort_entries_match({"city": user_input[CONF_CITY], "interval": user_input[CONF_INTERVAL]})
            return self.async_create_entry(
                title=user_input[CONF_CITY], data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_CITY, default=DEFAULT_CITY): str,
                    vol.Required(CONF_INTERVAL, default=DEFAULT_INTERVAL): int,
                }
            ),
        )

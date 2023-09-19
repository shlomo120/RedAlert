DOMAIN = "redalert"  # Replace with your integration's domain

async def async_setup(hass, config):
    """Set up the Red Alert integration."""
    hass.data.setdefault(DOMAIN, {})
    return True

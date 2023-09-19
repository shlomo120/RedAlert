# Red Alert Custom Integration for Home Assistant

This custom integration for Home Assistant allows you to receive Red Alert emergency alerts specific to your city.

![Red Alert Logo](https://w17.snunit.k12.il/snunit_catalog/files/uploads/users/visual/FFFF_FFFF_2017_04_27_12_52_23.png)

## Installation

### HACS (Home Assistant Community Store)

If you have [HACS](https://hacs.xyz/) installed, you can easily add this integration to Home Assistant by following these steps:

1. Open the HACS dashboard in your Home Assistant UI.
2. Search for "Red Alert" in the Integration tab.
3. Click "Install" next to the Red Alert integration.
4. Configure the integration with your city name and other settings via the Home Assistant Configuration UI.

### Manual Installation

To manually install the Red Alert integration, follow these steps:

1. Copy the `redalert` directory to your Home Assistant custom components directory.
   - If you don't have a `custom_components` directory in your Home Assistant configuration directory, create it.

2. Configure the integration with your city name and other settings via the Home Assistant Configuration UI.

## Configuration

To configure the Red Alert integration, follow these steps:

1. In your configuration.yaml file, add the configuration for your integration under the sensor section:

`Configuration.yaml:`
```
sensor:
  - platform: redalert
    city: "תל אביב"  # Specify your chosen city here
```

2. Adjust the city value to match your chosen city.
   The list of cities as identified in the plugin can be found in `cities.txt`

4. After adding the configuration to your configuration.yaml file, save the file and restart your Home Assistant instance to apply the changes.

5. Once Home Assistant has restarted, you should be able to see the sensor in your Home Assistant user interface under the "Developer Tools" > "States" section. Look for a sensor with a name like `sensor.redalert` .
The sensor will display the state True or False depending on whether there is an active alert for the specified city.

6. Once configured, you can add the Red Alert sensor to your Home Assistant dashboard.

## Usage

The Red Alert sensor will display emergency alerts specific to your city. Alerts will be updated at regular intervals (as specified in your configuration).



 ## Troubleshooting 

  If you encounter any issues or have questions about this integration, feel free to reach out on the [Home Assistant community forums](https://community.home-assistant.io/). 

<!--## Contributing -->

<!-- Contributions to this project are welcome. If you'd like to contribute, please follow the guidelines in our [CONTRIBUTING.md](CONTRIBUTING.md) file. -->

<!-- ## License  -->

<!-- This integration is licensed under the [MIT License](LICENSE). --> 

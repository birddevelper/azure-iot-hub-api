# azure-iot-hub-api
Azure IoT hub api interface using azure cli

This package is alternative to [azure-iot-hub](https://pypi.org/project/azure-iot-hub/) which hasn't had any updates in several years and relays on the deprecated [azure-uamqp-python](https://github.com/Azure/azure-uamqp-python).

This package can be used as a stopgap until the [azure-iot-hub](https://pypi.org/project/azure-iot-hub/) been updated to no longer depend on deprecated packages.

Currently these very basic functionalities of the **IoTHubRegistryManager** are supported:

- **create_device_with_sas**
- **get_twin**
- **get_twins**
- **update_twin**
- **get_device**
- **get_devices**
- **delete_device**

The package are designed, so that, if it is used as alternative to existing azure-iot-hub in the project, it need to make only little changes to the codebase.

## Usage

Install package :

```bash
pip install azure-iot-hub-api
```

Simply import and create ``IoTHubRegistryManager`` using connection string, then you can call api functions.

## Sample code

```python
from azure_iot_hub_api import IoTHubRegistryManager

AZURE_IOT_CONNECTION_STRING = "HostName=MyAzureIotHub.azure-devices.net;SharedAccessKeyName=xxx;SharedAccessKey=xxxxxxxxxxxxxx"
registry_manager = IoTHubRegistryManager(AZURE_IOT_CONNECTION_STRING)
my_device_id = 'E-11'
primary_key = 'primary-base64-key'
secondary_key = 'secondary-base64-key'

# Create a device
registry_manager.create_device_with_sas(
        device_id=my_device_id,
        primary_key=primary_key,
        secondary_key=secondary_key,
        status='enabled',
    )

# Get device twin
my_device_twin = registry_manager.get_twin(device_id=my_device_id)
my_device_twin.properties.desired['speed'] = 70

# Update device twin (It updates only desired object)
registry_manager.update_twin(device_id=my_device_id, twin=my_device_twin)

```






import json
import tempfile
from typing import List
from azure.cli.core import get_default_cli

from .models import Device, Twin
from .utilities import _ensure_quoted


class IoTHubRegistryManager:
    def __init__(self, connection_string: str):
        self.cli = get_default_cli()
        self.connection_string = connection_string

    def _invoke(self, command: str) -> dict:
        with tempfile.TemporaryFile(mode = "w") as temp:
            azure_cli_args = command.split()
            self.cli.invoke(azure_cli_args, out_file=temp)
        
            if self.cli.result.error:
                raise self.cli.result.error

            return self.cli.result.result

    def get_twin(self, device_id: str) -> Twin:
        """Gets a device twin.

        :param str device_id: The name (Id) of the device.

        :returns: The Twin object.
        """
        cmd = f"iot hub device-twin show --device-id {device_id} --login {self.connection_string}"
        result = self._invoke(cmd)
        return Twin.from_dictionary(result)

    def update_twin(self, device_id: str, twin: Twin, etag=None) -> Twin:

        """Updates tags and desired properties of a device twin.

        :param str device_id: The name (Id) of the device.
        :param Twin device_twin: The twin info of the device.
        :param str etag: The etag (if_match) value to use for the update operation.

        :returns: The Twin object.
        """
        if etag is None:
            etag = "*"
        etag = _ensure_quoted(etag)
        twin_properties_desired = "".join(json.dumps(twin.properties.desired).split())
        cmd = (
            f"iot hub device-twin update --device-id {device_id} "
            f"--login {self.connection_string} --desired {twin_properties_desired} --etag {etag}"
        )
        result = self._invoke(cmd)
        return Twin.from_dictionary(result)

    def create_device_with_sas(
        self, device_id: str, primary_key: str, secondary_key: str, status: str
    ) -> Device:
        """Creates a device identity on IoTHub that will use SAS as authentication method.

        :param str device_id: The name (Id) of the device.
        :param str primary_key: Primary authentication key.
        :param str secondary_key: Secondary authentication key.
        :param str status: Initial state of the created device.
            (Possible values: "enabled" or "disabled").

        :returns: Device object containing the created device.
        """
        cmd = (
            f"iot hub device-identity create --device-id {device_id} --primary-key {primary_key} "
            f"--secondary-key {secondary_key} --status {status} --login {self.connection_string}"
        )
        return Device.from_dictionary(self._invoke(cmd))


    def delete_device(self, device_id: str, etag=None) -> None:
        """Deletes a device identity from IoTHub.

        :param str device_id: The name (Id) of the device.
        :param str etag: The etag (if_match) value to use for the delete operation.

        :returns: None.
        """
        if etag is None:
            etag = "*"

        etag = _ensure_quoted(etag)
        cmd = (
            f"iot hub device-identity delete --device-id {device_id} "
            f"--login {self.connection_string} --etag {etag}"
        )
        self._invoke(cmd)



    def get_devices(self, max_number_of_devices:int=-1) -> List[Device]:
        """Get the identities of multiple devices from the IoTHub identity
           registry.

        :param int max_number_of_devices: This parameter when specified, defines the maximum number
           of device identities that are returned. Any value outside the range of
           1-1000 is considered to be 1000. Default value is -1 which means unlimited.

        :returns: List of device info.
        """
        cmd = (
            f"iot hub device-identity list --top {max_number_of_devices}"
            f" --login {self.connection_string}"
        )

        result = self._invoke(cmd)
        devices = [ Device.from_dictionary(device) for device in result ]

        return devices


    def get_twins(self, max_number_of_device_twins:int=-1) -> List[Twin]:
        """Get the twins of multiple devices from the IoTHub identity
           registry.

        :param int max_number_of_device_twins: This parameter when specified, defines the maximum number
           of device twins that are returned. Any value outside the range of
           1-1000 is considered to be 1000. Default value is -1 which means unlimited.

        :returns: List of device info.
        """
        cmd = (
            f"iot hub device-twin list --top {max_number_of_device_twins}"
            f" --login {self.connection_string}"
        )

        result = self._invoke(cmd)
        twins = [ Twin.from_dictionary(device) for device in result ]

        return twins
    


    def get_device(self, device_id:str) -> Device:
        """Retrieves a device identity from IoTHub.

        :param str device_id: The name (Id) of the device.

        :returns: The Device object containing the requested device.
        """
        cmd = f"iot hub device-identity show --device-id {device_id} --login {self.connection_string}"
        result = self._invoke(cmd)
        return Device.from_dictionary(result)
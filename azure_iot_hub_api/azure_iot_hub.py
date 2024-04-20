import json
import tempfile
from azure.cli.core import get_default_cli

from .models import Device, Twin


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
        cmd = f"iot hub device-twin show --device-id {device_id} --login {self.connection_string}"
        result = self._invoke(cmd)
        return Twin.from_dictionary(result)

    def update_twin(self, device_id: str, twin: Twin) -> Twin:
        twin_properties_desired = "".join(json.dumps(twin.properties.desired).split())
        cmd = (
            f"iot hub device-twin update --device-id {device_id} "
            f"--login {self.connection_string} --desired {twin_properties_desired}"
        )
        result = self._invoke(cmd)
        return Twin.from_dictionary(result)

    def create_device_with_sas(
        self, device_id: str, primary_key: str, secondary_key: str, status: str
    ) -> Device:
        cmd = (
            f"iot hub device-identity create --device-id {device_id} --primary-key {primary_key} "
            f"--secondary-key {secondary_key} --status {status} --login {self.connection_string}"
        )
        return Device.from_dictionary(self._invoke(cmd))

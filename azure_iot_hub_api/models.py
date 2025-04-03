from datetime import datetime
from dateutil import parser as datetime_parser


class Device:
    def __init__(
        self,
        device_id: str,
        generation_id: str = None,
        etag: str = None,
        connection_state=None,
        status: str = None,
        status_reason: str = None,
        connection_state_updated_time: datetime = None,
        status_updated_time: datetime = None,
        last_activity_time: datetime = None,
        cloud_to_device_message_count: int = None,
        authentication: dict = None,
        capabilities: dict = None,
        device_scope: str = None,
        parent_scopes: list[str] = None,
    ):
        self.device_id = device_id
        self.generation_id = generation_id
        self.etag = etag
        self.connection_state = connection_state
        self.status = status
        self.status_reason = status_reason
        self.connection_state_updated_time = connection_state_updated_time
        self.status_updated_time = status_updated_time
        self.last_activity_time = last_activity_time
        self.cloud_to_device_message_count = cloud_to_device_message_count
        self.authentication = authentication
        self.capabilities = capabilities
        self.device_scope = device_scope
        self.parent_scopes = parent_scopes

    @staticmethod
    def from_dictionary(device_dictionary: dict) -> 'Device':
        device_id = device_dictionary.get('deviceId')
        generation_id = device_dictionary.get("generationId")
        etag = device_dictionary.get("etag")
        connection_state = device_dictionary.get("connectionState")
        status = device_dictionary.get("status")
        status_reason = device_dictionary.get("statusReason")
        connection_state_updated_time = datetime_parser.parse(
            device_dictionary.get('connectionStateUpdatedTime') or "0001-01-01T00:00:00.000-00:00"
        )
        status_updated_time = datetime_parser.parse(
            device_dictionary.get("statusUpdatedTime") or "0001-01-01T00:00:00.000-00:00"
            )
        last_activity_time = datetime_parser.parse(
            device_dictionary.get('lastActivityTime') or "0001-01-01T00:00:00.000-00:00"
            )
        cloud_to_device_message_count = device_dictionary.get("cloudToDeviceMessageCount")
        authentication = device_dictionary.get('authentication')
        capabilities = device_dictionary.get('capabilities')
        device_scope = device_dictionary.get('deviceScope')
        parent_scopes = device_dictionary.get('parentScopes')

        return Device(
            device_id=device_id,
            generation_id=generation_id,
            etag=etag,
            connection_state=connection_state,
            status=status,
            status_reason=status_reason,
            connection_state_updated_time=connection_state_updated_time,
            status_updated_time=status_updated_time,
            last_activity_time=last_activity_time,
            cloud_to_device_message_count=cloud_to_device_message_count,
            authentication=authentication,
            capabilities=capabilities,
            device_scope=device_scope,
            parent_scopes=parent_scopes,
        )

    def to_dictionary(self) -> dict:
        return {
            "deviceId": self.device_id,
            "generationId": self.generation_id,
            "etag": self.etag,
            "connectionState": self.connection_state,
            "status": self.status,
            "statusReason": self.status_reason,
            "connectionStateUpdatedTime": (
                self.connection_state_updated_time.isoformat() if self.connection_state_updated_time else None
            ),
            "statusUpdateTime": self.status_updated_time.isoformat() if self.status_updated_time else None,
            "lastActivityTime": self.last_activity_time.isoformat() if self.last_activity_time else None,
            "cloudToDeviceMessageCount": self.cloud_to_device_message_count,
            "authentication": self.authentication,
            "capabilities": self.capabilities,
            "device_scope": self.device_scope,
            "parent_scopes": self.parent_scopes,
        }


class TwinProperties:
    def __init__(self, desired: dict, reported: dict):
        self.desired = desired
        self.reported = reported

    @staticmethod
    def from_dictionary(properties_dictionary: dict) -> 'TwinProperties':
        desired = properties_dictionary.get("desired")
        reported = properties_dictionary.get("reported")
        return TwinProperties(desired=desired, reported=reported)

    def to_dictionary(self) -> dict:
        return {"desired": self.desired, "reported": self.reported}


class Twin:
    def __init__(
        self,
        device_id: str,
        model_id: str,
        properties: TwinProperties,
        etag: str,
        version: int,
        device_etag: str,
        status: str,
        status_update_time: datetime,
        connection_state: str,
        last_activity_time: datetime,
        cloud_to_device_message_count: int,
        authentication_type: str,
        x509_thumbprint: dict,
        capabilities: dict,
        device_scope: str = None,
        parent_scopes=None,
        status_reason: str = None,
        tags: dict = None,
        module_id: str = None,
    ):
        self.device_id = device_id
        self.model_id = model_id
        self.tags = tags
        self.properties = properties
        self.etag = etag
        self.version = version
        self.device_etag = device_etag
        self.status = status
        self.status_reason = status_reason
        self.status_update_time = status_update_time
        self.connection_state = connection_state
        self.last_activity_time = last_activity_time
        self.cloud_to_device_message_count = cloud_to_device_message_count
        self.authentication_type = authentication_type
        self.x509_thumbprint = x509_thumbprint
        self.capabilities = capabilities
        self.device_scope = device_scope
        self.parent_scopes = parent_scopes
        self.module_id = module_id

    @staticmethod
    def from_dictionary(twin_dictionary: dict) -> 'Twin':
        device_id = twin_dictionary.get("deviceId")
        model_id = twin_dictionary.get("modelId")
        tags = twin_dictionary.get("tags")
        properties = TwinProperties.from_dictionary(twin_dictionary.get("properties"))
        etag = twin_dictionary.get("etag")
        version = twin_dictionary.get("version")
        device_etag = twin_dictionary.get("deviceEtag")
        status = twin_dictionary.get("status")
        status_reason = twin_dictionary.get("statusReason")
        status_update_time = datetime_parser.parse(twin_dictionary.get("statusUpdateTime"))
        connection_state = twin_dictionary.get("connectionState")
        last_activity_time = datetime_parser.parse(twin_dictionary.get("lastActivityTime"))
        cloud_to_device_message_count = twin_dictionary.get("cloudToDeviceMessageCount")
        authentication_type = twin_dictionary.get("authenticationType")
        x509_thumbprint = twin_dictionary.get("x509Thumbprint")
        capabilities = twin_dictionary.get("capabilities")
        device_scope = twin_dictionary.get("deviceScope")
        parent_scopes = twin_dictionary.get("parentScopes")
        module_id = twin_dictionary.get('moduleId')
        return Twin(
            device_id=device_id,
            model_id=model_id,
            tags=tags,
            properties=properties,
            etag=etag,
            version=version,
            device_etag=device_etag,
            status=status,
            status_reason=status_reason,
            status_update_time=status_update_time,
            connection_state=connection_state,
            last_activity_time=last_activity_time,
            cloud_to_device_message_count=cloud_to_device_message_count,
            authentication_type=authentication_type,
            capabilities=capabilities,
            device_scope=device_scope,
            parent_scopes=parent_scopes,
            x509_thumbprint=x509_thumbprint,
            module_id=module_id,
        )

    def to_dictionary(self) -> dict:
        return {
            "deviceId": self.device_id,
            "modelId": self.model_id,
            "tags": self.tags,
            "properties": self.properties.to_dictionary(),
            "etag": self.etag,
            "version": self.version,
            "deviceEtag": self.device_etag,
            "status": self.status,
            "statusReason": self.status_reason,
            "statusUpdateTime": self.status_update_time.isoformat() if self.status_update_time else None,
            "connectionState": self.connection_state,
            "lastActivityTime": self.last_activity_time.isoformat() if self.last_activity_time else None,
            "cloudToDeviceMessageCount": self.cloud_to_device_message_count,
            "authenticationType": self.authentication_type,
            "x509Thumbprint": self.x509_thumbprint,
            "capabilities": self.capabilities,
            "deviceScope": self.device_scope,
            "parentScopes": self.parent_scopes,
            "moduleId": self.module_id,
        }

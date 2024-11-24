from datetime import datetime
from typing import Any
from uuid import UUID


class SensorDataType:
    TEMPERATURE = "TEMPERATURE"


class SensorData:
    id: UUID
    device_id: str
    type: SensorDataType
    value: Any
    timestamp: datetime

    def __init__(
        self,
        id: UUID,
        device_id: str,
        type: SensorDataType,
        value: Any,
        timestamp: datetime
    ):
        self.id = id
        self.device_id = device_id
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'id': self.id,
            'device_id': self.device_id,
            'type': self.type,
            'value': self.value,
            'timestamp': self.timestamp.isoformat()
        }

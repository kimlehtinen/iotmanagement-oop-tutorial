from abc import ABC, abstractmethod

from src.core.sensor.sensor_data import SensorData


class SensorDataRepository(ABC):
    @abstractmethod
    def get_by_device_id(self, device_id: str) -> list[SensorData]:
        pass

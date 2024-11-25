from abc import ABC, abstractmethod

from src.core.sensor.sensor_data import SensorData


class SensorDataRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[SensorData]:
        pass

    @abstractmethod
    def get_by_device_id(self, device_id: str) -> list[SensorData]:
        pass

    @abstractmethod
    def create(self, sensor_data: SensorData) -> SensorData:
        pass

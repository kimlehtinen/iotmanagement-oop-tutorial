from abc import ABC, abstractmethod

from src.core.device.device import Device


class DeviceRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Device]:
        pass

    @abstractmethod
    def get_by_id(self, device_id: str) -> Device:
        pass

    @abstractmethod
    def create(self, device: Device) -> Device:
        pass

    @abstractmethod
    def update(self, device: Device) -> Device:
        pass

    @abstractmethod
    def delete(self, device_id: str) -> bool:
        pass

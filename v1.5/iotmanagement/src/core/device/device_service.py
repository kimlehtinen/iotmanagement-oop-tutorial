from src.core.device.device_repository import DeviceRepository
from src.core.device.device import Device
from src.core.device.device_summary import DeviceSummary


class DeviceService:
    device_repository: DeviceRepository

    def __init__(self, device_repository: DeviceRepository):
        self.device_repository = device_repository

    def get_all(self) -> list[Device]:
        return self.device_repository.get_all()
    
    def get_device_summary(self, device_id: str) -> DeviceSummary:
        device = self.device_repository.get_by_id(device_id)
        device_summary = DeviceSummary(device=device)

    def create_device(self, device: Device) -> Device:
        return self.device_repository.create(device)   

    def delete_device(self, device_id: str) -> bool:
        return self.device_repository.delete(device_id)

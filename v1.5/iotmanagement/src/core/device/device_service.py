from src.core.device.device_repository import DeviceRepository
from src.core.device.device import Device
from src.core.device.device_summary import DeviceSummary
from src.core.device.device_summary_generator import DeviceSummaryGenerator


class DeviceService:
    device_repository: DeviceRepository
    device_summary_generator: DeviceSummaryGenerator

    def __init__(
        self,
        device_repository: DeviceRepository,
        device_summary_generator: DeviceSummaryGenerator
    ):
        self.device_repository = device_repository
        self.device_summary_generator = device_summary_generator

    def get_all_devices(self) -> list[Device]:
        return self.device_repository.get_all()
    
    def get_device_summary(self, device_id: str) -> DeviceSummary | None:
        device: Device = self.device_repository.get_by_id(device_id)
        if device is None:
            return None

        return self.device_summary_generator.generate(device)

    def create_device(self, device: Device) -> Device:
        existing_device = self.device_repository.get_by_id(device.id)
        if existing_device:
            raise ValueError(f"Device with id={device.id} already exists")

        return self.device_repository.create(device)   

    def delete_device(self, device_id: str) -> bool:
        return self.device_repository.delete(device_id)

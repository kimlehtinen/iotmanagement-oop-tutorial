from src.core.device.device import Device
from src.core.sensor.temperature_status import TemperatureStatus


class SensorDataSummary:
    latest_temp_status: TemperatureStatus
    latest_temp_value: float | None

    def __init__(
        self,
        latest_temp_status: TemperatureStatus = TemperatureStatus.UNKNOWN,
        latest_temp_value: float = None,
    ):
        self.latest_temp_status = latest_temp_status
        self.latest_temp_value = latest_temp_value


class DeviceSummary:
    device: Device
    sensor_data_summary: SensorDataSummary

    def __init__(
        self,
        device: Device,
        sensor_data_summary: SensorDataSummary
    ) -> None:
        self.device = device
        self.sensor_data_summary = sensor_data_summary

    def to_dict(self) -> dict:
        return {
            'device': self.device.to_dict(),
            'sensor_data_summary': {
                'temperature': {
                    'latest_status': self.sensor_data_summary.latest_temp_status.value,
                    'latest_value': self.sensor_data_summary.latest_temp_value,
                },
            }
        }

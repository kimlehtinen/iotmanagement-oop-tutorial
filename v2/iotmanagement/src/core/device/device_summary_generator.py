from src.core.sensor.sensor_data import SensorData, SensorDataType
from src.core.sensor.sensor_data_repository import SensorDataRepository
from src.core.device.device import Device
from src.core.device.device_summary import DeviceSummary, SensorDataSummary
from src.core.sensor.temperature_utils import TemperatureUtils


class DeviceSummaryGenerator:
    _sensor_data_repository: SensorDataRepository
    _temp_utils: TemperatureUtils

    def __init__(self, sensor_data_repository: SensorDataRepository) -> None:
        self._sensor_data_repository = sensor_data_repository
        self._temp_utils = TemperatureUtils()

    def generate(self, device: Device) -> DeviceSummary:
        sensor_data_points: list[SensorData] = self._sensor_data_repository.get_by_device_id(device.id)
    
        temperature_readings = list(filter(lambda x: x.type == SensorDataType.TEMPERATURE, sensor_data_points))
        temperature_readings.sort(key=lambda x: x.timestamp)

        sensor_summary = SensorDataSummary()

        if len(temperature_readings) > 0:
            sensor_summary.latest_temp_value = temperature_readings[-1].value
            sensor_summary.latest_temp_status = self._temp_utils.determine_status(sensor_summary.latest_temp_value)

        return DeviceSummary(device, sensor_summary)

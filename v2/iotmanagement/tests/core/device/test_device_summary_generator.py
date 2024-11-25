from uuid import UUID
import datetime

from src.core.device.device_summary_generator import DeviceSummaryGenerator
from src.core.sensor.sensor_data import SensorData, SensorDataType
from src.core.device.device import Device
from src.core.device.device_summary import DeviceSummary
from src.core.sensor.temperature_status import TemperatureStatus


def test_generate__creates_temp_summary_when_readings_found():
    device = Device(
        id="RASPBERRY_PI_000001",
        name="Raspberry Pi 1",
        location="Factory 1"
    )
    sensor_data = [
        SensorData(
            id=UUID("7853e7fd-d64d-48a4-b101-29d5017c836e"),
            device_id=device.id,
            type=SensorDataType.TEMPERATURE,
            value=10,
            timestamp=datetime.datetime(2024, 1, 1, 0, 0, 0)
        ),
        SensorData(
            id=UUID("a7585fff-2932-4527-9345-d76ca9947164"),
            device_id="RASPBERRY_PI_000002",
            type=SensorDataType.TEMPERATURE,
            value=20,
            timestamp=datetime.datetime(2024, 1, 1, 0, 0, 10)
        ),
        SensorData(
            id=UUID("927ed1de-523b-4447-8293-06f82576b7d8"),
            device_id=device.id,
            type=SensorDataType.TEMPERATURE,
            value=25,
            timestamp=datetime.datetime(2024, 1, 1, 0, 0, 20)
        )
    ]
    repository = MockSensorDataRepository(sensor_data)
    sut = DeviceSummaryGenerator(sensor_data_repository=repository)

    result: DeviceSummary = sut.generate(device)

    assert result.sensor_data_summary.latest_temp_value == 25
    assert result.sensor_data_summary.latest_temp_status == TemperatureStatus.NORMAL


def test_generate__creates_empty_summary_when_no_sensor_data_found():
    device = Device(
        id="RASPBERRY_PI_000001",
        name="Raspberry Pi 1",
        location="Factory 1"
    )
    repository = MockSensorDataRepository(sensor_data=[])
    sut = DeviceSummaryGenerator(sensor_data_repository=repository)

    result: DeviceSummary = sut.generate(device)

    assert result.sensor_data_summary.latest_temp_value == None
    assert result.sensor_data_summary.latest_temp_status == TemperatureStatus.UNKNOWN



class MockSensorDataRepository:
    def __init__(self, sensor_data: list[SensorData]):
        self.sensor_data = sensor_data

    def get_by_device_id(self, device_id: str) -> list[SensorData]:
        return list(filter(lambda x: x.device_id == device_id, self.sensor_data))

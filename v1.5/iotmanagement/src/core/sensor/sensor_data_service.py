from src.core.sensor.sensor_data_repository import SensorDataRepository
from src.core.sensor.sensor_data import SensorData

class SensorDataService:
    sensor_data_repository: SensorDataRepository

    def __init__(self, sensor_data_repository: SensorDataRepository):
        self.sensor_data_repository = sensor_data_repository

    def get_all_sensor_data(self) -> list[SensorData]:
        return self.sensor_data_repository.get_all()

    def create_sensor_data(self, sensor_data: SensorData) -> SensorData:
        return self.sensor_data_repository.create(sensor_data)

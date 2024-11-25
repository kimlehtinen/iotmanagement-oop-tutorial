from datetime import datetime
from uuid import UUID
import requests
from src.core.sensor.sensor_data_repository import SensorDataRepository
from src.core.sensor.sensor_data import SensorData, SensorDataType

class SensorApiClient(SensorDataRepository):
    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_all(self) -> list[SensorData]:
        response: requests.Response = requests.get(f'{self.base_url}/sensor-data')
        if not response.ok:
            raise Exception(f'Error getting sensor data: {response.status_code}')
        
        response_data = response.json()
        data_list: list[dict] = response_data['data']

        sensor_data_list: list[SensorData] = []
        for sensor_data_dict in data_list:
            sensor_data = SensorData(
                id=UUID(sensor_data_dict['id']),
                device_id=sensor_data_dict['device_id'],
                type=SensorDataType(sensor_data_dict['type']),
                value=sensor_data_dict['value'],
                timestamp=datetime.fromisoformat(sensor_data_dict['timestamp'])
            )
            sensor_data_list.append(sensor_data)
        
        return sensor_data_list
    
    def get_by_device_id(self, device_id: str) -> list[SensorData]:
        all_sensor_data: list[SensorData] = self.get_all()
        if not len(all_sensor_data) > 0:
            return None

        device_data = list(filter(lambda x: x.device_id == device_id, all_sensor_data))

        return device_data

    def create(self, sensor_data: SensorData) -> SensorData:
        """
        Ei enää tarvita, koska, laitteet lähettävät dataa suoraan Sensor API:in
        tämän IoT Management sovelluksen rajapinnan sijaan.
        """
        pass

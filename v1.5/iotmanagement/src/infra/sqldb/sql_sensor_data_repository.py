from sqlalchemy import text
from sqlalchemy.orm import Session
from src.core.sensor.sensor_data import SensorData
from src.core.sensor.sensor_data_repository import SensorDataRepository

class SQLSensorDataRepository(SensorDataRepository):
    db_session: Session

    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def get_by_device_id(self, device_id: str) -> list[SensorData]:
        rows = self.db_session.execute(
            text('SELECT id, device_id, type, value, timestamp FROM sensor_data WHERE device_id = :device_id'),
            {'device_id': device_id}
        ).fetchall()

        sensor_data_readings = []
        for row in rows:
            sensor_data = SensorData(
                id=row[0],
                device_id=row[1],
                type=row[2],
                value=row[3],
                timestamp=row[4]
            )
            sensor_data_readings.append(sensor_data)

        return sensor_data_readings

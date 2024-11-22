
import datetime
from sqlalchemy import text
from config.db import get_db_session
from models.device import Device
from enums.temperature_status import TemperatureStatus


def create_device(data) -> Device:
    """
    Huono esimerkki:
    - Kerrokset eivät ole selkeästi eroteltu
    - Tietokantaoperaatiot ja liiketoimintalogiikka ovat edelleen samassa paikassa
    - Vaikea testata
    """
    with get_db_session() as db_session:
        existing_device = db_session.execute(
            text('SELECT * FROM devices WHERE id = :id'),
            {'id': data['id']},
        ).fetchone()
        
        if existing_device:
            raise ValueError(f"Device with id={data['id']} already exists")

        db_session.execute(
            text('INSERT INTO devices (id, name, location) VALUES (:id, :name, :location)'),
            {'id': data['id'], 'name': data['name'], 'location': data['location']},
        )
        db_session.commit()

        return Device(
            id=data['id'],
            name=data['name'],
            location=data['location'],
        )


def get_device(device_id: str):
    """
    Huono esimerkki:
    - Kerrokset eivät ole selkeästi eroteltu
    - Tietokantaoperaatiot ja liiketoimintalogiikka ovat edelleen samassa paikassa
    - Vaikea testata
    """
    data = {}
    device = {}
    sensor_data = []
    with get_db_session() as db_session:
        device_row = db_session.execute(
            text('SELECT id, name, location FROM devices WHERE id = :id'),
            {'id': device_id},
        ).fetchone()
        
        if not device_row:
            return None

        device = {
            'id': device_row[0],
            'name': device_row[1],
            'location': device_row[2],
        }

        sensor_data_rows = db_session.execute(
            text('SELECT id, device_id, type, value, timestamp FROM sensor_data WHERE device_id = :device_id ORDER BY timestamp ASC'),
            {'device_id': device_id},
        ).fetchall()

        for sensor_data_row in sensor_data_rows:
            sensor_data.append({
                'id': sensor_data_row[0],
                'device_id': sensor_data_row[1],
                'type': sensor_data_row[2],
                'value': sensor_data_row[3]['value'],
                'timestamp': sensor_data_row[4].isoformat(),
            })

    temperature_data = list(filter(lambda x: x['type'] == 'TEMPERATURE', sensor_data))
    latest_temperature_status = TemperatureStatus.UNKNOWN
    latest_temperature_val = None

    if len(temperature_data) > 0:
        latest_temperature_val = temperature_data[-1]['value']
        if latest_temperature_val > 100:
            latest_temperature_status = TemperatureStatus.DANGER
        elif latest_temperature_val > 80:
            latest_temperature_status = TemperatureStatus.WARNING
        else:
            latest_temperature_status = TemperatureStatus.NORMAL
        

    data['device'] = device
    data['sensor_data_summary'] = {
        'temperature': {
            'latest_status': latest_temperature_status.value,
            'latest_value': latest_temperature_val
        }
    }

    return data



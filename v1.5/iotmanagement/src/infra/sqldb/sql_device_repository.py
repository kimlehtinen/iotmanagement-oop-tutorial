from sqlalchemy import text
from sqlalchemy.orm import Session

from iotmanagement.src.core.device.device_repository import DeviceRepository
from iotmanagement.src.core.device.device import Device


class SQLDeviceRepository(DeviceRepository):
    db_session: Session

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all(self) -> list[Device]:
        rows = self.db_session.execute(text('SELECT * FROM devices')).fetchall()
        devices = []
        for row in rows:
            device = Device(
                id=row['id'],
                name=row['name'],
                location=row['location']
            )
            devices.append(device)

        return devices

    def get_by_id(self, device_id) -> Device:
        row = self.db_session.execute(
            text('SELECT * FROM devices WHERE id = :id'),
            {'id': device_id}
        ).fetchone()

        if row is None:
            return None

        return Device(
            id=row['id'],
            name=row['name'],
            location=row['location']
        )

    def create(self, device) -> Device:
        self.db_session.execute(
            text('INSERT INTO devices (id, name, location) VALUES (:id, :name, :location)'),
            {'id': device.id, 'name': device.name, 'location': device.location}
        )

        return self._get_by_id_or_fail(device.id)

    def update(self, device) -> Device:
        self.db_session.execute(
            text('UPDATE devices SET name = :name, location = :location WHERE id = :id'),
            {'id': device.id, 'name': device.name, 'location': device.location}
        )

        return self._get_by_id_or_fail(device.id)

    def delete(self, device_id) -> bool:
        self.db_session.execute(
            text('DELETE FROM devices WHERE id = :id'),
            {'id': device_id}
        )

        return True
    
    def _get_by_id_or_fail(self, device_id) -> Device:
        device = self.get_by_id(device_id)
        if device is None:
            raise Exception('Device not found')

        return device


from sqlalchemy import text
from config.db import get_db_session
from models.device import Device


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

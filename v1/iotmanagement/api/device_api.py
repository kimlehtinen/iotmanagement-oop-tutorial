from flask import Blueprint, jsonify, request
from sqlalchemy import text

from config.db import get_db_session
from utils import device_utils
from models.device import Device

device_api = Blueprint('device_api', __name__)


@device_api.route('/device', methods=['GET'])
def get_device():
    """
    Huono esimerkki:
    - Kerrokset eivät ole selkeästi eroteltu
    - Rajapinta, tietokantaoperaatiot ja liiketoimintalogiikka ovat samassa paikassa
    - Vaikea testata
    """
    with get_db_session() as db_session:
        rows = db_session.execute(text('SELECT id, name, location FROM devices')).fetchall()
        devices = []
        for row in rows:
            print(row)
            devices.append({
                'id': row[0],
                'name': row[1],
                'location': row[2],
            })

        return {'devices': devices}


@device_api.route('/device', methods=['POST'])
def create_device():
    """
    Parannus:
    + Rajapinta ja tietokantaoperaatiot eroteltu
    + Liiketoimintalogiikka eroteltu 
    """
    data = request.json
    
    try:
        device: Device = device_utils.create_device(data)
    except ValueError as e:
        return {"message": str(e)}, 400

    response = {
        'id': device.id,
        'name': device.name,
        'location': device.location,
    }

    return jsonify(response), 201
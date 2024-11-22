import uuid
from flask import Blueprint, jsonify, request
from sqlalchemy import text

from config.db import get_db_session


sensor_api = Blueprint('sensor_api', __name__)

@sensor_api.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    """
    Huono esimerkki:
    - Rajapinta, tietokantaoperaatiot ja liiketoimintalogiikka ovat samassa paikassa
    - Vaikea testata
    """
    result = []
    with get_db_session() as db_session:
        rows = db_session.execute(
            text('SELECT * FROM sensor_data')
        ).fetchall()

        for row in rows:
            result.append({
                'id': row['id'],
                'device_id': row['device_id'],
                'value': row['value']['value'],
                'type': row['type'],
                'timestamp': row['timestamp']
            })

    return jsonify(result), 200


@sensor_api.route('/sensor-data', methods=['POST'])
def post_sensor_data():
    sensor_data = request.json

    with get_db_session() as db_session:
        sensor_data_id = uuid.uuid4()
        db_session.execute(
            text('INSERT INTO sensor_data (id, device_id, value, type) VALUES (:device_id, :value)'),
            {
                'id': sensor_data_id,
                'device_id': sensor_data['device_id'],
                'value': {'value': sensor_data['value']},
                'type': sensor_data['type']
            }
        )

        data = db_session.execute(
            text('SELECT * FROM sensor_data WHERE id = :id'),
            {'id': sensor_data_id}
        ).fetchone()

    return jsonify(data), 201

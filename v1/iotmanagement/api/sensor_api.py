from datetime import datetime
import json
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
            text('SELECT id, device_id, value, type, timestamp FROM sensor_data ORDER BY timestamp ASC')
        ).fetchall()

        for row in rows:
            tstamp: datetime = row[4]
            result.append({
                'id': row[0],
                'device_id': row[1],
                'value': row[2]['value'],
                'type': row[3],
                'timestamp': tstamp.isoformat()
            })

            print("Type:", type(row[4]))

    return jsonify(result), 200


@sensor_api.route('/sensor-data', methods=['POST'])
def post_sensor_data():
    sensor_data = request.json
    with get_db_session() as db_session:
        sensor_data_id = uuid.uuid4()
        db_session.execute(
            text('INSERT INTO sensor_data (id, device_id, value, type) VALUES (:id, :device_id, :value, :type)'),
            {
                'id': sensor_data_id,
                'device_id': sensor_data['device_id'],
                'value': json.dumps({'value': sensor_data['value']}),
                'type': sensor_data['type']
            }
        )
        db_session.commit()
        row = db_session.execute(
            text('SELECT id, device_id, value, type, timestamp FROM sensor_data WHERE id = :id'),
            {'id': sensor_data_id}
        ).fetchone()

        data = {
            'id': row[0],
            'device_id': row[1],
            'value': row[2]['value'],
            'type': row[3],
            'timestamp': row[4].isoformat()
        }

    return jsonify(data), 201

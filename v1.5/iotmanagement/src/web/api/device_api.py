
from flask import Blueprint


device_api = Blueprint('device_api', __name__)


@device_api.route('/device', methods=['GET'])
def get_device():
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


@device_api.route('/device/<device_id>', methods=['GET'])
def get_device_by_id(device_id: str):
    data = device_utils.get_device(device_id)
    if not data:
        return jsonify({"message": "Not found"}), 404
    
    return jsonify(data), 200


@device_api.route('/device/<device_id>', methods=['DELETE'])
def delete_device(device_id: str):
    with get_db_session() as db_session:
        db_session.execute(
            text('DELETE FROM devices WHERE id = :device_id'), 
            {'device_id': device_id}
        )
        db_session.commit()

    return jsonify({"message": "Device deleted"}), 200


import datetime
import os
import uuid
from flask import Flask, json, jsonify, request

app = Flask(__name__)

sensor_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sensor_data.json'))


@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    sensor_data = {"data": []}
    if os.path.exists(sensor_data_path):
        with open(sensor_data_path) as f:
            sensor_data = json.load(f)

    return jsonify(sensor_data), 200


@app.route('/sensor-data', methods=['POST'])
def post_sensor_data():
    payload = request.json
    sensor_data = {
        "id": str(uuid.uuid4()),
        "device_id": payload["device_id"],
        "type": payload["type"],
        "value": payload["value"],
        "timestamp": datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
    }

    all_data = {"data": []}
    if os.path.exists(sensor_data_path):
        with open(sensor_data_path) as f:
            all_data = json.load(f)
            if not isinstance(all_data, dict):
                all_data = {"data": []}
            if "data" not in all_data:
                all_data["data"] = []

    all_data["data"].append(sensor_data)

    with open(sensor_data_path, 'w') as f:
        json.dump(all_data, f)

    return jsonify(sensor_data), 201

if __name__ == '__main__':
    app.run(port=5070, debug=True)

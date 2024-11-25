from datetime import datetime
import uuid
from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from src.config.di_container import DIContainer
from src.core.sensor.sensor_data_service import SensorDataService
from src.core.sensor.sensor_data import SensorData, SensorDataType


sensor_api = Blueprint('sensor_api', __name__)

@sensor_api.route('/sensor-data', methods=['GET'])
@inject
def get_sensor_data(
    sensor_data_service: SensorDataService = Provide[DIContainer.sensor_data_service]
):
    sensor_data: list[SensorData] = sensor_data_service.get_all_sensor_data()

    result: list[dict] = [data.to_dict() for data in sensor_data]

    return jsonify(result), 200


@sensor_api.route('/sensor-data', methods=['POST'])
@inject
def post_sensor_data(
    sensor_data_service: SensorDataService = Provide[DIContainer.sensor_data_service]
):
    data = request.json

    sensor_data = SensorData(
        id=uuid.uuid4(),
        device_id=data['device_id'],
        value=data['value'],
        type=SensorDataType(data['type']),
        timestamp=datetime.now()
    )

    sensor_data_service.create_sensor_data(sensor_data)

    return jsonify(sensor_data.to_dict()), 201




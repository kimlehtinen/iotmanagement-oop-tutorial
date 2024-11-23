
from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide

from src.core.device.device import Device
from src.core.device.device_service import DeviceService
from src.core.device.device_summary import DeviceSummary
from src.config.di_container import DIContainer

device_api = Blueprint('device_api', __name__)


@device_api.route('/device', methods=['GET'])
@inject
def get_device(
    device_service: DeviceService = Provide[DIContainer.device_service]
):
    devices: list[Device] = device_service.get_all()
    devices_dict: list[dict] = list(map(lambda x: x.to_dict(), devices))

    return jsonify(devices_dict), 200


@device_api.route('/device', methods=['POST'])
def create_device(
    device_service: DeviceService = Provide[DIContainer.device_service]
):
    data = request.json

    device = Device(
        id=data['id'],
        name=data['name'],
        location=data['location']
    )

    device = device_service.create_device(device)

    return jsonify(device.to_dict()), 201


@device_api.route('/device/<device_id>', methods=['GET'])
def get_device_by_id(
    device_id: str,
    device_service: DeviceService = Provide[DIContainer.device_service]
):
    device_summary: DeviceSummary = device_service.get_device_summary(device_id)
    if not device_summary:
        return jsonify({"message": "Not found"}), 404
    
    return jsonify(device_summary.to_dict()), 200


@device_api.route('/device/<device_id>', methods=['DELETE'])
def delete_device(
    device_id: str,
    device_service: DeviceService = Provide[DIContainer.device_service]
):
    is_deleted: bool = device_service.delete_device(device_id)
    if not is_deleted:
        return jsonify({"message": "Unexpected error when deleting"}), 500

    return jsonify({"message": "Device deleted"}), 200


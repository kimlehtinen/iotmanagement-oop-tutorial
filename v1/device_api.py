
from flask import Blueprint


device_api = Blueprint('device_api', __name__)


@device_api.route('/device', methods=['GET'])
def get_device():
    return ['device1', 'device2', 'device3']

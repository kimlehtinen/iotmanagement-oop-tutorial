
from flask import Blueprint, render_template


device_pages = Blueprint('device_pages', __name__)

@device_pages.route('/', methods=['GET'])
def get_devices():
    return render_template('index.html')

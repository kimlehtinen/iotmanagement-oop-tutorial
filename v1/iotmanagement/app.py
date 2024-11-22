from flask import Flask

from api.device_api import device_api
from api.sensor_api import sensor_api
from config.db import DATABASE_URL
from pages.device_pages import device_pages

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.register_blueprint(device_api)
app.register_blueprint(sensor_api)
app.register_blueprint(device_pages)

if __name__ == '__main__':
    app.run(port=5050, debug=True)

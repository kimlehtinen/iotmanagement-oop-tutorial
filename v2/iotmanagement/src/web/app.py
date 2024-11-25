import os
from flask import Flask

from src.config.di_container import DIContainer

def create_app():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print("Root dir: ", root_dir)
    template_dir = os.path.join(root_dir, 'web/html/templates')
    static_dir = os.path.join(root_dir, 'web/html/static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    from src.infra.sqldb.db import DATABASE_URL
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    
    from src.web.api import device_api
    from src.web.api import sensor_api
    from src.web.html.pages.device_pages import device_pages

    di_container = DIContainer()
    di_container.wire(modules=[
        device_api,
        sensor_api
    ])

    app.register_blueprint(device_api.device_api)
    app.register_blueprint(sensor_api.sensor_api)
    app.register_blueprint(device_pages)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)

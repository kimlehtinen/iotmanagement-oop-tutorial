from flask import Flask

from src.config.di_container import DIContainer

def create_app():
    app = Flask(__name__)
    from src.web.api.device_api import device_api

    di_container = DIContainer()
    di_container.wire(modules=[
        device_api
    ])

    app.register_blueprint(device_api)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)

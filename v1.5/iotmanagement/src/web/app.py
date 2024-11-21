from flask import Flask

def create_app():
    app = Flask(__name__)
    from iotmanagement.src.web.api.device_api import device_api
    app.register_blueprint(device_api)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)

# IoT Management

## Introduction
Showing why clean code and architecture is important, and how OOP can be used to achieve that.

Versions:
- [v1](/v1): 
    - Showcasing bad examples
    - Framework code, APIs, business logic, database calls all mixed together.
    - Code is difficult to read, test and maintain.
    - Difficult to add new features, make changes to code and architecture.
- [v1.5](/v1.5)
    - Same high-level architecture as v1, but clean code and architecture taken into use.
    - Increased readability, testability and maintenance.
- [v2](/v2)
    - Based on v1.5
    - Architecture change: sensor data is moved its own service/application.
    - Nothing changed from our main application's perspective.
    - Same interfaces, just new implementations.

## Local environment setup

### Clone project
```
git clone
```

### Create virtual env
```
python -m venv iotenv
```

On Linux, activate:
```
source iotvenv/bin/activate
```

On Windows activate:
```
.\iotvenv\Scripts\activate.bat
```

### Install dependencies
```
pip install -r requirements.txt
```

## Run V1 IoT Management
```
cd v1/iotmanagement/
python app.py
```

## Run V1.5 IoT Management
```
cd v1.5/iotmanagement/
python -m flask --app src.web.app:create_app run --host=127.0.0.1 --port=5055 --debug
```

## Run V2 IoT Management

### Iot Management
```
cd v2/iotmanagement/
python -m flask --app src.web.app:create_app run --host=127.0.0.1 --port=5065 --debug
```

### Sensor API
```
cd v2/sensorapi/
python server.py
```

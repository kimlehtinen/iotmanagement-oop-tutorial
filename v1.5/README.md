# IoT Management - V1.5

- Shows how using OOP and clean architecture fixes the mess we have in [V1](../v1).
- Code is more maintainable, extendable and testable.
- Appropriate abstractions make it easy to migrate from [V1 Architecture](#v1-architecture) to [V2 Architecture](#v2-architecture).


## V1 Architecture
![V1 Architecture](./v1architecture.png)

## V2 Architecture
![V1 Architecture](./v2architecture.png)

## Setup
Install dependencies
```
pip install -r requirements.txt
```

## Run development server
```
cd v1.5/iotmanagement/
python -m flask --app src.web.app:create_app run --host=127.0.0.1 --port=5055 --debug
```


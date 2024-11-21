# IoT Management

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
cd v1
python app.py
```

## Run V2 IoT Management
```
cd v2

python iotmanagement/src/flask/app.py
```

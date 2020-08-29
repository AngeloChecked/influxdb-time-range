# Influxdb test

> a influxdb fast time range exploration.

## Requirements

```
- docker
- python3
- pip
```

## Install influxdb docker image

```sh
docker pull influxdb
```

## Run database

```sh
scripts/run-influxdb
```

## Run database client 
```sh
scripts/influx-client-console
```

## Run python test script
```sh
cd app
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 time-range.py
deactivate
```

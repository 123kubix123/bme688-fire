import random
import pickle

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sklearn.neural_network import MLPClassifier

app = FastAPI()

origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class MinSensorData(BaseModel):
    temperature: float  # -40 - 85 C
    pressure: float  # 300 - 1200 hPa
    humidity: float  # 0 - 100 %
    gas_resistance: float  # 0 - 100 Ohm
    air_quality: float  # 0 - 500 IAQ


class SensorData(MinSensorData):
    status: Optional[float]  # 0 - 100 %
    meas_index: Optional[float]  # 0 - 100 %
    fire_detected: bool


classifier: MLPClassifier = pickle.load(open('finalized_model.sav', 'rb'))

sensor_data_1 = SensorData(
    temperature=round(random.random() * 125 - 40, 3),
    pressure=round(random.random() * 900 + 300, 3),
    humidity=round(random.random() * 100, 3),
    gas_resistance=round(random.random() * 100, 3),
    air_quality=round(random.random() * 500, 3),
    fire_detected=False
)

sensor_data_2 = SensorData(
    temperature=round(random.random() * 125 - 40, 3),
    pressure=round(random.random() * 900 + 300, 3),
    humidity=round(random.random() * 100, 3),
    gas_resistance=round(random.random() * 100, 3),
    air_quality=round(random.random() * 500, 3),
    fire_detected=False
)

show_data_1 = True


@app.get("/sensor_data", response_model=SensorData, response_model_exclude_unset=True)
def get_sensor_data() -> SensorData:
    global sensor_data_1
    global sensor_data_2
    global show_data_1

    if show_data_1:
        return sensor_data_1
    else:
        return sensor_data_2


@app.post("/update_data")
def update_data(data: MinSensorData):
    global sensor_data_1
    global sensor_data_2
    global show_data_1
    global classifier

    fire_detected = bool(classifier.predict([[data.temperature, data.pressure, data.humidity]]))
    new_data = SensorData(
            temperature=data.temperature,
            pressure=data.pressure,
            humidity=data.humidity,
            gas_resistance=data.gas_resistance,
            air_quality=data.air_quality,
            fire_detected=fire_detected
        )

    if show_data_1:
        sensor_data_2 = new_data
        show_data_1 = False
    else:
        sensor_data_1 = new_data
        show_data_1 = True

from pydantic import BaseModel
from datetime import datetime


class Client(BaseModel):
    # id: str
    name: str | None = None
    lastName: str | None = None
    email: str | None = None
    # createdAt: datetime | None = None
    # updatedAt: datetime | None = None
    # deletedAt: datetime | None = None


class Module(BaseModel):
    # id: str
    userId: str | None = None
    name: str | None = None
    # createdAt: datetime | None = None
    # updatedAt: datetime | None = None
    # deletedAt: datetime | None = None


class SensorData(BaseModel):
    # id: str
    sensorId: str | None = None
    temperature: float
    pH: float | None = None
    tds: float | None = None
    turbidity: float | None = None
    # createdAt: datetime | None = None


class Sensor(BaseModel):
    # id: str
    moduleId: str | None = None
    # createdAt: datetime | None = None
    # updatedAt: datetime | None = None
    # deletedAt: datetime | None = None

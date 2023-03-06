import logging
import pathlib

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes import view_clients, view_modules, view_sensor_data, view_sensors

ROOT = pathlib.Path(__file__).resolve().parent  # app/
BASE_DIR = ROOT.parent
LOGDIR_CFG = f"{BASE_DIR}/logging.conf"
logging.config.fileConfig(LOGDIR_CFG, disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Air Quality API 🌬️",
    description="REST API to measure air quality",
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index() -> dict[str, str]:
    return {
        "info": "This is the index page of BusGeolocationAPI. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


app.include_router(view_clients.router)
app.include_router(view_modules.router)
app.include_router(view_sensors.router)
app.include_router(view_sensor_data.router)

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import logging
import pathlib

from app.routes import views


ROOT = pathlib.Path(__file__).resolve().parent  # app/
BASE_DIR = ROOT.parent
LOGDIR_CFG = f'{BASE_DIR}/logging.conf'
logging.config.fileConfig(LOGDIR_CFG, disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(views.router)

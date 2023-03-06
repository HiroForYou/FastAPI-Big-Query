from __future__ import annotations

import logging

from google.cloud import bigquery
from google.oauth2 import service_account

from app.core.config import get_keyfile_dict

logger = logging.getLogger(__name__)


def get_client_connection():
    key_json = get_keyfile_dict()
    client = None
    logger.info("Trying to connect to API 1..")
    try:
        credentials = service_account.Credentials.from_service_account_info(key_json)
        client = bigquery.Client(
            credentials=credentials,
            project=credentials.project_id,
        )

        logger.info("API 1: Success Connected")
    except Exception as err:
        logging.error("An error occurred while trying to connect to API 1: %s", err)
        raise err

    return client


if __name__ == "__main__":
    get_client_connection()

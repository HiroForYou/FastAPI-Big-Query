from __future__ import annotations
import logging

from app.apis.big_query.connection import get_client_connection
from app.core.config import PROJECT_ID, DATASET_NAME

logger = logging.getLogger(__name__)


def get_last_n_data(n: int) -> list:
    client = get_client_connection()
    query = f"""
        SELECT * FROM `{PROJECT_ID}.{DATASET_NAME}.sensorData` ORDER BY createdAt DESC LIMIT {n}
    """
    logger.info("Getting the last %d data from sensors..", n)
    logger.info("query>> %s", query)
    results = []
    try:
        query_job = client.query(query)
        for idx, row in enumerate(query_job):
            if idx == 0:
                keys = tuple(row.keys())
                results.append(keys)
            results.append(row.values())
    except Exception as err:
        logging.error("failed BQ job %s", err)
        raise err
    return results


def get_initial_n_data(n: int) -> list:
    client = get_client_connection()
    query = f"""
        SELECT * FROM `{PROJECT_ID}.{DATASET_NAME}.sensorData` ORDER BY createdAt ASC LIMIT {n}
    """
    logger.info("Getting the first %d data from sensors..", n)
    logger.info("query>> %s", query)
    results = []
    try:
        query_job = client.query(query)
        for idx, row in enumerate(query_job):
            if idx == 0:
                keys = tuple(row.keys())
                results.append(keys)
            results.append(row.values())
    except Exception as err:
        logging.error("failed BQ job %s", err)
        raise err
    return results


if __name__ == "__main__":
    print(get_last_n_data(1))
    print(get_initial_n_data(3))

from __future__ import annotations
import logging

from app.apis.big_query.connection import get_client_connection
from app.apis.big_query.utils import charify
from app.core.config import PROJECT_ID, DATASET_NAME


logger = logging.getLogger(__name__)


def create_sensor_data(item_encoded: dict) -> list:
    connection = get_client_connection()
    keys, values = item_encoded.keys(), list(item_encoded.values())
    values = list(map(charify, values))
    keys_string, values_string = ", ".join(keys), ", ".join(values)
    query = f"""INSERT INTO `{PROJECT_ID}.{DATASET_NAME}.sensorData` (id, {keys_string}, createdAt) VALUES (GENERATE_UUID(), {values_string}, CURRENT_TIMESTAMP());"""

    logger.info("Creating new sensor data..")
    logger.info("query>> %s", query)
    try:
        query_job = connection.query(query)
        info_msg = f"Success creation {query_job}"
        logger.info("response >> %s", info_msg)
        return info_msg
    except Exception as err:
        logging.error("failed BQ job %s", err)
        raise err


def get_last_n_sensor_data(n: int) -> list:
    connection = get_client_connection()
    query = f"""
        SELECT * FROM `{PROJECT_ID}.{DATASET_NAME}.sensorData` ORDER BY createdAt DESC LIMIT {n}
    """
    logger.info("Getting the last %d data from sensors..", n)
    logger.info("query>> %s", query)

    try:
        results = []
        query_job = connection.query(query)
        for idx, row in enumerate(query_job):
            if idx == 0:
                keys = tuple(row.keys())
                results.append(keys)
            results.append(row.values())
        info_msg = f"Success getting last {query_job}"
        logger.info("response >> %s", info_msg)
        return results
    except Exception as err:
        logging.error("failed BQ job %s", err)
        raise err


def get_initial_n_sensor_data(n: int) -> list:
    connection = get_client_connection()
    query = f"""
        SELECT * FROM `{PROJECT_ID}.{DATASET_NAME}.sensorData` ORDER BY createdAt ASC LIMIT {n}
    """
    logger.info("Getting the first %d data from sensors..", n)
    logger.info("query>> %s", query)

    try:
        results = []
        query_job = connection.query(query)
        for idx, row in enumerate(query_job):
            if idx == 0:
                keys = tuple(row.keys())
                results.append(keys)
            results.append(row.values())
        info_msg = f"Success getting initial {query_job}"
        logger.info("response >> %s", info_msg)
        return results
    except Exception as err:
        logging.error("failed BQ job %s", err)
        raise err


def update_sensor_data_by_id(id: str, item_encoded: dict) -> list:
    connection = get_client_connection()
    keys, values = item_encoded.keys(), item_encoded.values()
    values = list(map(charify, values))
    item_string = [f"{key}={value}" for key, value in zip(keys, values)]
    item_string = ", ".join(item_string)
    query = f"""
        UPDATE `{PROJECT_ID}.{DATASET_NAME}.sensorData` SET {item_string} WHERE id='{id}'
    """
    logger.info("Updating sensor data with id %s..", id)
    logger.info("query>> %s", query)
    try:
        query_job = connection.query(query)
        info_msg = f"Success update {query_job}"
        logger.info("response >> %s", info_msg)
        return info_msg
    except Exception as err:
        logging.error("failed BQ job %s", err)
        raise err


def remove_sensor_data_by_id(id: str) -> list:
    connection = get_client_connection()
    query = f"""
        DELETE FROM `{PROJECT_ID}.{DATASET_NAME}.sensorData` WHERE id='{id}'
    """
    logger.info("Removing sensor data with id %s..", id)
    logger.info("query>> %s", query)
    try:
        query_job = connection.query(query)
        info_msg = f"Success remove {query_job}"
        logger.info("response >> %s", info_msg)
        return info_msg
    except Exception as err:
        logging.error("failed BQ job %s", err)
        raise err


if __name__ == "__main__":
    print(get_last_n_sensor_data(1))
    print(get_initial_n_sensor_data(3))

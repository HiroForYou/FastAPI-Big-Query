from __future__ import annotations

from google.cloud import bigquery
from google.oauth2 import service_account

from app.core.config import get_keyfile_dict

# TODO(developer): Set key_path to the path to the service account key
#                  file.
""" key_path = "./smartcity-ks.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
) """



# Alternatively, use service_account.Credentials.from_service_account_info()
# to set credentials directly via a json object rather than set a filepath
# TODO(developer): Set key_json to the content of the service account key file.
# credentials = service_account.Credentials.from_service_account_info(key_json)

key_json = get_keyfile_dict()
credentials = service_account.Credentials.from_service_account_info(key_json)

client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id,
)

query = """
    SELECT * FROM `smartcity-379119.smart_city_dataset.sensorData` LIMIT 3
"""
query_job = client.query(query)  # Make an API request.

print("The query data:")
for row in query_job:
    # Row values can be accessed by field name or index.
    print(row)
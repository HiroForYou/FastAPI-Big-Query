import pathlib
from starlette.config import Config

ROOT = pathlib.Path(__file__).resolve().parent.parent  # app/
BASE_DIR = ROOT.parent  # ./

config = Config(BASE_DIR / ".env")

def get_keyfile_dict():
    variables_keys = {
        "type": config("TYPE", str),
        "project_id": config("PROJECT_ID", str), 
        "private_key_id": config("PRIVATE_KEY_ID", str), 
        "private_key": config("PRIVATE_KEY", str).replace('\\n', '\n'), 
        "client_email": config("CLIENT_EMAIL", str),
        "client_id": config("CLIENT_ID", str),
        "auth_uri": config("AUTH_URI", str), 
        "token_uri": config("TOKEN_URI", str), 
        "auth_provider_x509_cert_url": config("AUTH_PROVIDER_X509_CERT_URL", str),
        "client_x509_cert_url": config("CLIENT_X509_CERT_URL", str)
    }
    return variables_keys

PROJECT_ID = config("PROJECT_ID", str)
DATASET_NAME = config("DATASET_NAME", str)
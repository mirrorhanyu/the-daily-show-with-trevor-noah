import json
import os


def create_google_secret_account_credential():
    credential = {
        "type": os.getenv('TYPE', ''),
        "project_id": os.getenv('PROJECT_ID', ''),
        "private_key_id": os.getenv('PRIVATE_KEY_ID', ''),
        "private_key": os.getenv('PRIVATE_KEY', ''),
        "client_email": os.getenv('CLIENT_EMAIL', ''),
        "client_id": os.getenv('CLIENT_ID', ''),
        "auth_uri": os.getenv('AUTH_URI', ''),
        "token_uri": os.getenv('TOKEN_URI', ''),
        "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_X509_CERT_URL', ''),
        "client_x509_cert_url": os.getenv('CLIENT_X509_CERT_URL', '')
    }
    with open('google_drive_service_account.json', 'w') as file:
        json.dump(credential, file, indent=2)

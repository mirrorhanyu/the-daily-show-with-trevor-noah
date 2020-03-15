import json
import os

from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GoogleDriveHelper:
    def __init__(self):
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
        auth = GoogleAuth()
        scope = ['https://www.googleapis.com/auth/drive']
        auth.credentials = ServiceAccountCredentials.from_json_keyfile_name('google_drive_service_account.json', scope)
        self.drive = GoogleDrive(auth)

    def upload(self, file_name, folder):
        file = self.drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder}]})
        file.SetContentFile(file_name)
        file.Upload()


google_drive = GoogleDriveHelper()

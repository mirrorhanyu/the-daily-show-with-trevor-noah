import json
import os

from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# https://developers.google.com/drive/api/v2/reference/files#resource-representations

class GoogleDriveHelper:
    def __init__(self):
        if not os.path.exists('google_drive_service_account.json'):
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

    def upload(self, file_name, description, folder):
        file = self.drive.CreateFile({
            'description': description,
            'parents': [{'kind': 'drive#fileLink', 'id': folder}]}
        )
        file.SetContentFile(file_name)
        file.Upload()

    def create_folder_inside(self, parent_folder, sub_folder_name):
        folder = self.drive.CreateFile({
            'title': sub_folder_name,
            'parents': [{'id': parent_folder}],
            "mimeType": "application/vnd.google-apps.folder"
        })
        folder.Upload()
        return folder['id']


google_drive = GoogleDriveHelper()

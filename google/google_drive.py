import json
import os

from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from settings import settings


# https://developers.google.com/drive/api/v2/reference/files#resource-representations

class GoogleDriveHelper:
    def __init__(self):
        if not os.path.exists('google_drive_service_account.json'):
            credential = {
                "type": settings.TYPE,
                "project_id": settings.PROJECT_ID,
                "private_key_id": settings.PRIVATE_KEY_ID,
                "private_key": settings.PRIVATE_KEY,
                "client_email": settings.CLIENT_EMAIL,
                "client_id": settings.CLIENT_ID,
                "auth_uri": settings.AUTH_URI,
                "token_uri": settings.TOKEN_URI,
                "auth_provider_x509_cert_url": settings.AUTH_PROVIDER_X509_CERT_URL,
                "client_x509_cert_url": settings.CLIENT_X509_CERT_URL
            }
            with open('google_drive_service_account.json', 'w') as file:
                json.dump(credential, file, indent=2)
        auth = GoogleAuth()
        scope = ['https://www.googleapis.com/auth/drive']
        auth.credentials = ServiceAccountCredentials.from_json_keyfile_name('google_drive_service_account.json', scope)
        self.drive = GoogleDrive(auth)

    def upload(self, file_name, description, folder):
        file = self.drive.CreateFile({
            'title': os.path.basename(file_name),
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

from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def _google_drive():
    auth = GoogleAuth()
    scope = ['https://www.googleapis.com/auth/drive']
    auth.credentials = ServiceAccountCredentials.from_json_keyfile_name('google_drive_service_account.json', scope)
    return GoogleDrive(auth)


def upload(file_name, folder):
    drive = _google_drive()
    file = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder}]})
    file.SetContentFile(file_name)
    file.Upload()

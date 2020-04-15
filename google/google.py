import glob

from google.google_drive import google_drive
from google.google_email import send_email
from settings import settings

daily_show_folder_id = '1Ghgv4WWsm330PXBC0OJ5GxRdVjfQ9afZ'


def upload_files_to_drive_by(entry):
    folder = google_drive.create_folder_inside(parent_folder=daily_show_folder_id, sub_folder_name=entry.title)
    for file in glob.glob('download/*'):
        google_drive.upload(file_name=file, description=entry.google_drive_details, folder=folder)


def send_notify_email(subject):
    send_email(from_address=settings.GOOGLE_EMAIL_USERNAME,
               to_address=settings.GOOGLE_NOTIFIED_EMAIL,
               subject=subject,
               text='Done!')

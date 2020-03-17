import os
import glob

from google.google_drive import google_drive
from google.google_email import send_email

daily_show_folder_id = '1vAn92qcBDwaZLc7dbqqdaqwSbszJw1cw'


def upload_files_to_drive_by(entry):
    # title of downloaded video are 80 long, and without words after separator |
    folder = google_drive.create_folder_inside(parent_folder=daily_show_folder_id, sub_folder_name=entry.title)
    for file in glob.glob(f'{entry.title_with_80_limit}*.*'):
        google_drive.upload(file, folder)


def send_notify_email(subject):
    send_email(from_address= os.getenv('GOOGLE_EMAIL_USERNAME'),
               to_address=os.getenv('GOOGLE_NOTIFIED_EMAIL'),
               subject=subject,
               text='Done!')

import os
import glob

from google.google_drive import google_drive
from google.google_email import send_email


def upload_files_to_drive_by(video_title):
    folder_id = '1vAn92qcBDwaZLc7dbqqdaqwSbszJw1cw'
    # title of downloaded video are 80 long, and without words after separator |
    file_name = video_title.split(" | ")[0][:80]
    for file in glob.glob(f'{file_name}*.*'):
        google_drive.upload(file, folder_id)


def send_notify_email(subject):
    send_email(from_address= os.getenv('GOOGLE_EMAIL_USERNAME'),
               to_address=os.getenv('GOOGLE_NOTIFIED_EMAIL'),
               subject=subject,
               text='Done!')

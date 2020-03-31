from time import sleep

from bilibili.bilibili import upload_files_to_bilibili
from google.google import send_notify_email, upload_files_to_drive_by
from utils.file_utils import remove_folder
from utils.time_utils import is_within_minutes
from video.video import generate_video_with_subtitle
from youtube.youtube import fetch_youtube_feed_entries, download

latest_youtube_entries = [entry for entry in fetch_youtube_feed_entries() if is_within_minutes(entry.published, minutes=30)]
for entry in latest_youtube_entries:
    download(entry.video_id)
    generate_video_with_subtitle()
    upload_files_to_drive_by(entry)
    upload_files_to_bilibili(entry)
    send_notify_email(f'[Youtube Downloaded & Uploaded] - {entry.title}')
    # sleep 30 seconds to avoid bilibili upload issue
    sleep(30)
    remove_folder('download')

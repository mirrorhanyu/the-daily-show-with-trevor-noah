from bilibili.bilibili import upload_files_to_bilibili
from google.google import send_notify_email, upload_files_to_drive_by
from utils.time_utils import is_within_hours
from youtube.youtube import fetch_youtube_feed_entries, download

entries = fetch_youtube_feed_entries()

for entry in entries:
    if is_within_hours(entry.published, hours=4):
        download(entry.video_id)
        upload_files_to_drive_by(entry)
        upload_files_to_bilibili(entry)
        send_notify_email(f'[Youtube Downloaded & Uploaded] - {entry.title}')

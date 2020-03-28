import glob

from bilibiliupload import VideoPart

from bilibili.bilibili_upload import bilibili_upload
from utils.file_utils import is_video

entertainment_video_type = 71
tags = ['综艺', '脱口秀', 'YOUTUBE搬运', '英语听力', 'YOUTUBE', '英语学习', '美国', '英语', '欧美']
source = 'http://www.youtube.com'


def upload_files_to_bilibili(entry):
    title = f'#崔娃今夜秀# {entry.title}'.split(" | ")[0][:80]
    video_paths = [path for path in glob.glob('download/*') if is_video(path)]
    video_to_be_uploaded = next((path for path in video_paths if '[WITH-SUBTITLE]' in path), video_paths[0])
    bilibili_upload.upload(parts=[VideoPart(path=video_to_be_uploaded, title=title, desc=entry.media_description)],
                           title=title,
                           tid=entertainment_video_type,
                           tag=tags,
                           desc=entry.bilibili_details,
                           source=source,
                           cover='',
                           dynamic='')

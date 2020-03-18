import glob

from bilibiliupload import VideoPart

from bilibili.bilibili_upload import bilibili_upload
from utils.file_utils import is_video

entertainment_video_type = 71
tags = ['综艺', '脱口秀', 'YOUTUBE搬运', '英语听力', 'YOUTUBE', '英语学习', '美国', '英语', '欧美']
source = 'http://www.youtube.com'


def upload_files_to_bilibili(entry):
    title = entry.title_with_80_limit
    # video_path = next(path for path in glob.glob(f'{title}*.*') if is_video(path))
    video_path = glob.glob(f'{title}*.*m*')[0]
    bilibili_upload.upload(parts=[VideoPart(path=video_path, title=title, desc=entry.media_description)],
                           title=title,
                           tid=entertainment_video_type,
                           tag=tags,
                           desc=entry.media_description,
                           source=source,
                           cover='',
                           dynamic='')

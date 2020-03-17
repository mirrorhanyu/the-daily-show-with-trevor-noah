import os

from bilibiliupload import Bilibili

bilibili_upload = Bilibili()
bilibili_upload.login(os.getenv('BILIBILI_USERNAME', ''), os.getenv('BILIBILI_PASSWORD', ''))

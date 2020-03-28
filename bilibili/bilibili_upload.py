from bilibiliupload import Bilibili

from settings import settings

bilibili_upload = Bilibili()
bilibili_upload.login(settings.BILIBILI_USERNAME, settings.BILIBILI_PASSWORD)

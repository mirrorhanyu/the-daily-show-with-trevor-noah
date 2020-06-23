from bilibiliupload import Bilibili

from settings import settings


def get_bilibili_upload():
    bilibili_upload = Bilibili()
    bilibili_upload.login(settings.BILIBILI_USERNAME, settings.BILIBILI_PASSWORD)
    return bilibili_upload

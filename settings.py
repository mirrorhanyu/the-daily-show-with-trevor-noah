import os


class Settings:
    def __init__(self):
        self.TYPE = os.getenv('TYPE', '')
        self.PROJECT_ID = os.getenv('PROJECT_ID', '')
        self.PRIVATE_KEY_ID = os.getenv('PRIVATE_KEY_ID', '')
        self.PRIVATE_KEY = os.getenv('PRIVATE_KEY', '')
        self.CLIENT_EMAIL = os.getenv('CLIENT_EMAIL', '')
        self.CLIENT_ID = os.getenv('CLIENT_ID', '')
        self.AUTH_URI = os.getenv('AUTH_URI', '')
        self.TOKEN_URI = os.getenv('TOKEN_URI', '')
        self.AUTH_PROVIDER_X509_CERT_URL = os.getenv('AUTH_PROVIDER_X509_CERT_URL', '')
        self.CLIENT_X509_CERT_URL = os.getenv('CLIENT_X509_CERT_URL', '')
        self.GOOGLE_EMAIL_USERNAME = os.getenv('GOOGLE_EMAIL_USERNAME', '')
        self.GOOGLE_EMAIL_PASSWORD = os.getenv('GOOGLE_EMAIL_PASSWORD', '')
        self.GOOGLE_NOTIFIED_EMAIL = os.getenv('GOOGLE_NOTIFIED_EMAIL', '')
        self.BILIBILI_COOKIE = os.getenv('BILIBILI_COOKIE', '')


settings = Settings()

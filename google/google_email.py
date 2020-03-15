import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename


def send_email(from_address, to_address, subject, text, attachments=None):
    server = smtplib.SMTP_SSL(host='smtp.googlemail.com', port=465)
    server.login(os.getenv('GOOGLE_EMAIL_USERNAME', ''), os.getenv('GOOGLE_EMAIL_PASSWORD', ''))

    content = MIMEMultipart()
    content['From'] = from_address
    content['To'] = to_address
    content['Subject'] = subject

    content.attach(MIMEText(text))

    for attachment in attachments or []:
        with open(attachment, 'rb') as file:
            content_attachment = MIMEApplication(file.read())
        content_attachment['Content-Disposition'] = f'attachment; filename={basename(attachment)}'
        content.attach(content_attachment)

    server.sendmail(from_address, to_address, content.as_string())
    server.close()

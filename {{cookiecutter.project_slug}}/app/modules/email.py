from aiosmtplib import SMTP

from app import settings

client = SMTP(hostname=settings.email.HOST, port=settings.email.PORT,)

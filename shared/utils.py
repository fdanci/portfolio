from decouple import config
from django.core.mail import send_mail, BadHeaderError
import logging

logger = logging.getLogger(__name__)


def send_contact_email(name, email, subject, message):
    message = f"Name: {name}\nEmail: {email}\n\n{message}"
    try:
        logger.info('Sending email...')
        send_mail(subject, message, config('EMAIL'), ['florin.danci96@gmail.com'])
    except BadHeaderError as err:
        logger.error('utils.send_contact_email(...)')
        logger.error(err)
    else:
        logger.info('Email has been sent!')

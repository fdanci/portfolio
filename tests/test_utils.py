from django.core import mail
from django.test import TestCase

from decouple import config


class TestEmail(TestCase):

    def test_send_email(self):
        """Test if sending email doesn't fail."""
        mail.send_mail('Subject test', 'This is a test message.',
                       config('EMAIL'), ['florin.danci96@gmail.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject test')

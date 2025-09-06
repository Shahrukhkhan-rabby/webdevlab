import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class EmailSender:

    def __init__(self):
        pass

    def send_activation_email(self, user, activation_link):
        subject = 'Activate Your Account'
        html_message = render_to_string('activation_email.html', {'activation_link': activation_link})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = user.email

        send_mail(
            subject,
            plain_message,
            from_email,
            [to_email],
            html_message=html_message,
        )
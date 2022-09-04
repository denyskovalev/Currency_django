
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_contact_us_email(subject, from_email):
    email_subject = 'ContactUs from Currency Project'
    body = f'''
            Subject from client: {subject}
            Email: {from_email}
            Wants to contact
                '''

    send_mail(
        email_subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )

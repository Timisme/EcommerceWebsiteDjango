from cgitb import html
from distutils.command.config import config
import celery
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from django.conf import settings

@celery.shared_task
def send_email():
    if not settings.ENABLE_EMAIL:
        return  

    context = {

    }

    html_body = render_to_string(
        'email.html',
        context= context
    )

    to_emails = ['tim@data-sci.info']

    # Create an email instance  
    email = EmailMultiAlternatives(
        subject = 'hi',
        from_email = 'tim@data-sci.info',
        to = ['tim@data-sci.info']
    )

    with get_connection(
        host = settings.EMAIL_HOST,
        port = settings.EMAIL_PORT,
        username = settings.EMAIL_HOST_USER,
        password = settings.EMAIL_HOST_PASSWORD,
        use_tls= settings.EMAIL_USE_TLS
    ) as connection:
        email.connection = connection
        email.attach_alternative(html_body, "text/html")
        email.send(fail_silently= False)
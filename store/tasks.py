import celery
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string

@celery.shared_task
def send_email():
    
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


logger = get_task_logger(__name__)


@shared_task(bind=True, name='send_registration_email')
def send_registration_email(self, context):
    try:
        subject = 'Uma nova inscrição'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = ['marcelolemesgalli@hotmail.com']
        html_content = render_to_string('emails/registration_email.html', context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()

        logger.info(f"Email sent to {to_email}")
    except Exception as e:
        logger.error(f"Error sending email to {to_email}: {e}")
        self.retry(exc=e, countdown=60, max_retries=3)

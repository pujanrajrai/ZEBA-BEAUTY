
from core.settings import EMAIL_HOST_USER
from home.models import Email

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class SendEmail:
    def __init__(self):
        self.host_email = EMAIL_HOST_USER

    def send_email_to_client(self, email, subject, body_var):
        html_content = render_to_string('email.html', body_var)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(
            subject, text_content, EMAIL_HOST_USER, email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def send_email_to_admin(self, subject, body_var):
        html_content = render_to_string('admin_email.html', body_var)
        text_content = strip_tags(html_content)
        recipient_list = []  # Add your own email address here
        other_email = Email.objects.all()
        for email in other_email:
            recipient_list.append(email.email)
        msg = EmailMultiAlternatives(
            subject, text_content, EMAIL_HOST_USER, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

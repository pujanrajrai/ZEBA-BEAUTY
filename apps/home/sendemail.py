
from core.settings import EMAIL_HOST_USER
from home.models import Email

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading


class SendEmail:
    def __init__(self):
        self.host_email = EMAIL_HOST_USER

    def send_email_to_client(self, email, subject, body_var):
        def send():

            html_content = render_to_string('email.html', body_var)
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(
                subject, text_content, self.host_email, email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        threading.Thread(target=send).start()

    def send_email_to_admin(self, subject, body_var):
        def send():
            html_content = render_to_string('admin_email.html', body_var)
            text_content = strip_tags(html_content)

            # Create a flat list of email addresses
            recipient_list = [
                email.email for email in Email.objects.all() if email.email]

            if recipient_list:
                for recipient in recipient_list:
                    try:
                        msg = EmailMultiAlternatives(
                            subject, text_content, self.host_email, [recipient])
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        print(f"Email sent to {recipient}")
                    except Exception as e:
                        print(f"Failed to send email to {recipient}: {e}")
            else:
                print("No valid recipients found.")

        threading.Thread(target=send).start()

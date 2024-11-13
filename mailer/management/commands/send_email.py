from django.core.management.base import BaseCommand
import smtplib
import ssl
from django.urls import reverse
from django.conf import settings

class Command(BaseCommand):
    help = 'Send a test email with a link that leads to a form page'

    def handle(self, *args, **kwargs):
        # URL for the form page (update with your local or deployed URL)
        form_page_url = f"http://127.0.0.1:8000/fake-login/"

        # Create a custom SSL context that skips certificate verification
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls(context=context)
                server.login('buisnessnewsletter@gmail.com', 'zyiz nhrc mkuk qwcn')
                subject = "Test Email with Form Link"
                body = f"Click the link below to verify your account:\n\n{form_page_url}"
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail('buisnessnewsletter@gmail.com', 'saxenaishaan1@gmail.com', message)
            self.stdout.write(self.style.SUCCESS("Email sent successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to send email: {str(e)}"))

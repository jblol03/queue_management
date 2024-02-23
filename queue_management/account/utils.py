from django.core.mail import EmailMessage
from queue_management import settings

class Util:
  @staticmethod
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email=settings.EMAIL_HOST_USER,
      to=[data['to_email']],
      # reply_to=[from_email],

    )
    email.send()
import string
import random
from django.core.mail import EmailMessage
from django.core.mail import send_mail
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
  
  def generate_otp(length=6):
      characters = string.digits
      otp = ''.join(random.choice(characters) for _ in range(length))
      return otp
  
  def send_otp_email(email, otp):
    subject = 'Your OTP for Login'
    message = f'Your OTP is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
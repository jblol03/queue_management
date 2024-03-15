from django.contrib.auth.backends import BaseBackend
from .models import EndUser

class OTPAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, otp=None, **kwargs):
        if email is None or otp is None:
            return None
        
        try:
            user = EndUser.objects.get(email=email)
        except EndUser.DoesNotExist:
            return None
        
        # Check if the provided OTP matches the user's stored OTP
        if otp == user.otp:
            return user
        
        return None

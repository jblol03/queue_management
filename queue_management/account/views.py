from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer, EndUserSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from account.models import EndUser

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer, BrowsableAPIRenderer]
  serializer_class=UserRegistrationSerializer
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer, BrowsableAPIRenderer]
  serializer_class=UserLoginSerializer

  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Successful'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer, BrowsableAPIRenderer]
  serializer_class=UserProfileSerializer

  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer, BrowsableAPIRenderer]
  serializer_class=UserChangePasswordSerializer
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer, BrowsableAPIRenderer]
  serializer_class=SendPasswordResetEmailSerializer
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password reset link sent. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer, BrowsableAPIRenderer]
  serializer_class=UserPasswordResetSerializer
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)

class EndUserRegistration(APIView):
    def post(self, request):
        serializer = EndUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EndUserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if email:
            user = self.authenticate_user(email, otp)
            if user:
                return Response({'message': 'OTP authentication successful'}, status=status.HTTP_200_OK)
            else:
                # Generate a new OTP for the provided email
                try:
                    user = EndUser.objects.get(email=email)
                    user.generate_otp()
                    user.save()
                    return Response({'message': 'New OTP generated successfully', 'email': email,}, status=status.HTTP_200_OK)
                except EndUser.DoesNotExist:
                    return Response({'message': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)
        elif otp:
            return Response({'message': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Email and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)

    def authenticate_user(self, email, otp):
        try:
            user = EndUser.objects.get(email=email)
            if user.otp == otp:
                return user
        except EndUser.DoesNotExist:
            pass
        return None
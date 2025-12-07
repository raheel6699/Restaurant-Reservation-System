from .models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from utils.common import success_response, error_response
from reservation_system import settings
# Create your views here.


class CreateUser(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        try:
            user = self.serializer_class(data=request.data)
            if user.is_valid():
                user.save()
                return success_response(message="User created successfully")
            return error_response(message="Invalid data")
        except Exception as e:
            return error_response(message=str(e))


class LoginUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            username = request.data.get("username", None)
            password = request.data.get("password", None)
            user = authenticate(username=username, password=password)
            if user is not None:
                user = User.objects.get(username= user.username)
                response_data = {
                    'refresh': user.tokens()['refresh'],
                    'access': user.tokens()['access'],
                    "access_expires_in": str(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]),
                    "refresh_expires_in": str(settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"])
                }
                return success_response(data=response_data, message="User logged in successfully.")
            else:
                return error_response(message="Invalid credentials")
        except Exception as e:
            return error_response(message=str(e))



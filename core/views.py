from typing import Any, cast

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    UserSerializer,
)


class APIRootView(APIView):
    """
    API Root view showing available endpoints
    """

    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {
                "message": "BloomHub Backend API",
                "endpoints": {
                    "auth": {
                        "register": "POST /api/auth/register/",
                        "login": "POST /api/auth/login/",
                        "refresh": "POST /api/auth/refresh/",
                        "logout": "POST /api/auth/logout/",
                        "profile": "GET /api/auth/profile/",
                    },
                    "admin": "GET /admin/",
                },
            }
        )


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            assert user is not None
            refresh = RefreshToken.for_user(cast(User, user))
            token_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data,
            }
            return Response(token_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = cast(dict[str, Any], serializer.validated_data)
            try:
                user = User.objects.get(email=data["email"])
                user = authenticate(username=user.username, password=data["password"])
            except User.DoesNotExist:
                user = None

            if user:
                refresh = RefreshToken.for_user(cast(User, user))
                token_data = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": UserSerializer(user).data,
                }
                return Response(token_data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class TokenRefreshViewCustom(TokenRefreshView):
    """
    Custom refresh view that returns user data along with new tokens
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200 and response.data:
            # Add user data to response
            user = request.user
            response.data["user"] = UserSerializer(user).data
        return response

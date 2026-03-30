import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    def post(self, request):
        logger.info("Registration request received with data")
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            logger.info("User registered successfully: %s", user.username)
            return Response({"user":{
                "username": user.username,
                "email": user.email,
                "role": user.role
            },
                "access": str(refresh.access_token),
              "refresh": str(refresh)
            }, status=status.HTTP_201_CREATED)
        logger.warning("Registration request failed with errors")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


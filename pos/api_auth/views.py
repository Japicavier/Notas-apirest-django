from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': True,
                'content': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'fullname': f"{user.first_name} {user.last_name}",
                    'token': str(refresh.access_token),
                }

            })
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

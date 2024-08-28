from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class LogIn(APIView):

    def post(self,request):
        password = request.data.get('password')
        username = request.data.get('username')

        user :User | None = authenticate(
            username = username,
            password=password
        )
        if user:
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'data': token.key},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'Invalid_Credential','detail':'Invalid username or password'}, status=status.HTTP_404_NOT_FOUND)

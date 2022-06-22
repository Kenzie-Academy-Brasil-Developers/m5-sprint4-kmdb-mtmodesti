from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status
from users.serializers import LoginSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    def post(self, request):
        
        serializer = RegisterSerializer(data=request.data)
     
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    
class LoginView(APIView):
    def post(self, request):
        print('toiiasd')
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED
        )
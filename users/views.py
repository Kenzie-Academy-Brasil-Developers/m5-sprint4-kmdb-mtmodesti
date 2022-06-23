from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status
from users.serializers import LoginSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from movies.permissions import IsOWner
from rest_framework.authentication import TokenAuthentication
from users.models import User
from users.serializers import RegisterSerializer

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
        
class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser, IsOWner]
    
    
    def get(self,request):
        
        users = User.objects.all()
        
        serializer = RegisterSerializer(users, many=True)
        
    
        
        
        return Response(serializer.data)
        
        
        
        
        return Response('rota de listar todos users')
    

class UserViewById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser, IsOWner]
    def get(self,request, user_id):
        return Response('rota de listar 1 user')
    
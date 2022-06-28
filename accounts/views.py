from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UserSerializer, LoginSerializer
from rest_framework import status
from accounts.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from accounts.permissions import AdmPermission


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})

        return Response(
            {"detail": "invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class ListAllUsers(APIView):

    permission_classes = [AdmPermission]

    def get(self, request):
        users = User.objects.all()
        serializer_response = UserSerializer(users, many=True)
        return Response(serializer_response.data)


class GetUser(APIView):

    permission_classes = [AdmPermission]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer_response = UserSerializer(user)
            return Response(serializer_response.data)
        except User.DoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status

from users.serializers import RegisterSerializer

from .models import User


class RegisterView(APIView):
    def post(self, request):
        
        serializer = RegisterSerializer(data=request.data)
        print(serializer)
        #serializer.is_valid(raise_exception=True)

       # serializer.save()

        # user = User.objects.create_superuser(**serializer.validated_data)

        # serializer = RegisterSerializer(user)
        return Response({"msg":"oi"})
       # return Response(serializer.data, status.HTTP_201_CREATED)

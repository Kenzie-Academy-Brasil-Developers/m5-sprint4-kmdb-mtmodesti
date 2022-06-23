from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from movies.serializers import RegisterMovieSerializer
from .models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from movies.permissions import IsOWner


class MoviesView(APIView):
    permission_classes = [IsAuthenticated, IsOWner]
    authentication_classes = [TokenAuthentication]

    def get(self, request):

        movies = Movie.objects.all()
        
        serializer = RegisterMovieSerializer(movies, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = RegisterMovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({"as": "rota de postar filme"})

from functools import partial
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, Response, status
from movies.serializers import RegisterMovieSerializer
from .models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from movies.permissions import IsOWner


class MoviesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser, IsOWner]

    def get(self, request):

        movies = Movie.objects.all()
        
        serializer = RegisterMovieSerializer(movies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterMovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)
    
    
class MovieIdView(APIView):
   
    
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = RegisterMovieSerializer(movie)
        return Response(serializer.data)
    
    def delete(self, request, movie_id):
         movie = get_object_or_404(Movie, pk=movie_id)
         movie.delete()
         return Response(status=204)
     
    def patch(self, request, movie_id):
        
        movie = get_object_or_404(Movie, pk=movie_id)
        
        serializer = RegisterMovieSerializer(movie, request.data, partial=True)
        
        serializer.is_valid(raise_exception=True)
        
        invalid_keys = ("genres")
        
        for key in serializer.validated_data.keys():
            if key in invalid_keys:
                return Response({"message" : f"You can not update {key} property."}, status=422)
            
        serializer.save()
        
        
        return Response(serializer.data)
        
     
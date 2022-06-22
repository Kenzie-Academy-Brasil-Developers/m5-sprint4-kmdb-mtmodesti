from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from movies.serializers import RegisterMovieSerializer
from .models import Movie

class MoviesView(APIView):
    def get(self,request):
        
        return Response({"as":"rota de listar filmes"})
        
    ...
    
    def post(self,request):
        
        serializer = RegisterMovieSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
      
        
        return Response({"as":"rota de postar filme"})
        
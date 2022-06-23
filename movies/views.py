from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from movies.serializers import RegisterMovieSerializer
from .models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from movies.permissions import IsAdmin, IsOWner

class MoviesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOWner]
    
    
    def get(self,request):
        
        return Response({"as":"rota de listar filmes"})
        
    ...
    
    def post(self,request):
        
         # Define qual o tipo de authenticação
         # Define quais as regras de permissão
        
        
        
        
        serializer = RegisterMovieSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
                  
        serializer.save()
        return Response({"as":"rota de postar filme"})
        
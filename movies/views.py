from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from movies.serializers import RegisterMovieSerializer

class MoviesView(APIView):
    def get(self,request):
        
        
        
        return Response({"as":"rota de listar filmes"})
        ...
    ...
    
    def post(self,request):
        
        serializer = RegisterMovieSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        return Response({"as":"rota de postar filmes"})
        
from rest_framework.views import APIView
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from movies.models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination


class ReviewView(APIView):
    
     def post(self, request, id):
    
        movie = get_object_or_404(Movie, pk=id)
        
        serializer = ReviewSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save(critic=request.user, movie=movie)

        return Response(serializer.data, status.HTTP_201_CREATED)
        
    
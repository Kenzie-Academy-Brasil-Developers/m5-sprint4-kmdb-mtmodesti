from rest_framework import serializers
from movies.models import Movie
from genres.serializers import RegisterGenreSerializer
from genres.models import Genre


class RegisterMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField()
    premiere = serializers.CharField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = RegisterGenreSerializer(many=True)
    
    def create(self, validated_data):
        
        genres_info = validated_data.pop("genres")
        
        movie = Movie.objects.create(**validated_data)
                
        for genre_type in genres_info:
                genre, _ = Genre.objects.get_or_create(**genre_type)
                movie.genres.add(genre)
                
        return movie

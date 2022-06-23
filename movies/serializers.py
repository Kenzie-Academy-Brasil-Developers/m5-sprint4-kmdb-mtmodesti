from rest_framework import serializers
from movies.models import Movie
from genres.serializers import RegisterGenreSerializer
from helpers.movies_helpers import Helper


class RegisterMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField()
    premiere = serializers.CharField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = serializers.ListField(
        child=RegisterGenreSerializer()
    )
    

    def create(self, validated_data):
        
        genres = validated_data.pop("genres")
        
        movie = Movie.objects.create(**validated_data)
        
        
        
        movie.genres.add(genres)
        
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        
        
        return Movie.objects.create(**validated_data)
    
        
    
    ''' 
    {
	"title":"Matrix",
	"duration":"175m",
	"premiere":"1972-09-10",
	"classification": 14,
	"synopsis":"resumo do filme",
	"genres": {"name":"ficção"}
}

    '''
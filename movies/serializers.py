from rest_framework import serializers
from movies.models import Movie


class RegisterMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField()
    premiere = serializers.CharField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = serializers.ListField(
        child=serializers.DictField(
            child = serializers.CharField(), allow_empty=False
            ), allow_empty=False
    )

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

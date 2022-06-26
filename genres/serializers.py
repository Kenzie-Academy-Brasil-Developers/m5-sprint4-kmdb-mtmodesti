from rest_framework import serializers
from genres.models import Genre


class RegisterGenreSerializer(serializers.Serializer):

    name = serializers.CharField()

    def create(self, validated_data: dict) -> Genre:
        genre, _ = Genre.objects.get_or_create(genre=genre)
        return genre
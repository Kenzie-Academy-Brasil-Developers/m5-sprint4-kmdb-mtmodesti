# books/serializers.py
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)

        model = Review
        fields = ["__all__"]

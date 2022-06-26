# books/serializers.py
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Review
        
        fields = ["stars", "review","spoilers","recomendation" ]
        
        read_only_fields = ["id"]
        
        
        
        
    def create(self, validated_data:dict) -> Review:
        return Review.objects.create(**validated_data)
    


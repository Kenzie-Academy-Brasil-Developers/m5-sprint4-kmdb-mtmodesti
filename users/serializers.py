from rest_framework import serializers
from users.models import User

class RegisterSerializer(serializers.Serializer):
    email = serializers.IntegerField(read_only=True)
    first_name = serializers.EmailField(max_length=100)
    last_name = serializers.CharField()
    updated_at = serializers.DateField()
    
    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("email já existe")

        return value
    
    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data) 


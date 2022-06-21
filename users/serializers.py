from rest_framework import serializers
from users.models import User


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=100)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    date_joined = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    
    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("email já existe")
        
        return value
    
    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data) 
    
   
    


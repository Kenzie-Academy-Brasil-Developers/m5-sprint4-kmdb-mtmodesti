from rest_framework import serializers
from accounts.models import User
from accounts.utils import CustomUserManager


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    updatedAt = serializers.DateTimeField(read_only=True)

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError("Email in use")
        except User.DoesNotExist as err:
            return email
        except serializers.ValidationError:
            raise serializers.ValidationError("Email already exists")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

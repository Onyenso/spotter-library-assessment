from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import CustomUser
from accounts.validators import validate_password

User: CustomUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            "first_name",
            "last_name",
            "tokens"
        ]

    def get_tokens(self, obj):
        jwt = RefreshToken.for_user(obj)
        return {"refresh": str(jwt), "access": str(jwt.access_token)}


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            'email',
            'password',
            "confirm_password",
        ]

    def validate(self, data):
        if not validate_password(data["password"]):
            raise serializers.ValidationError(
                {"password": "Password does not meet the requirements."}
            )

        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match.")

        return data


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
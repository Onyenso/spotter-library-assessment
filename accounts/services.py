import random
from typing import Any, Mapping

from django.contrib.auth import get_user_model

from accounts.models import CustomUser


User: CustomUser = get_user_model()


class UserService:
    @staticmethod
    def register_user(validated_data: Mapping[str, Any]):
        """This method registers a new user."""

        new_user: CustomUser = User.objects.create_user(
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data["email"]
        )

        return new_user

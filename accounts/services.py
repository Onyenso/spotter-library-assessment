import random
from typing import Any, List, Mapping, Optional

from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import transaction
from django.core.mail import send_mail
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.authtoken.models import Token

from accounts.models import CustomUser


User: CustomUser = get_user_model()


class UserService:
    @staticmethod
    def register_user(validated_data: Mapping[str, Any]) -> object:
        """This method registers a new user."""

        new_user: CustomUser = User.objects.create_user(
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data["email"]
        )

        return new_user
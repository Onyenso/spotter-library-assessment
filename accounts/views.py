from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action

from accounts.models import CustomUser

from accounts.serializers import (
    UserRegistrationSerializer,
    UserSerializer,
    UserLoginSerializer,
)
from accounts.services import UserService


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService().register_user(validated_data=serializer.validated_data)
        
        return Response(
            self.get_serializer(user).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response(
            self.get_serializer(user).data,
            status=status.HTTP_200_OK
        )
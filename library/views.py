from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

from library.models import Book, Author, Favorite
from library.permissions import IsOwnerOrReadOnly
from library.serializers import (
    AuthorSerializer,
    BookSerializer,
    CreateBookSerializer,
    CreateFavoriteSerializer,
    FavoriteSerializer
)
from library.services import LibraryService


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["title", "author__name"]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CreateBookSerializer
        return BookSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class FavoriteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def list(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateFavoriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        success, message = LibraryService.add_to_favorites(
            user=request.user,
            book_id=serializer.validated_data["book"].id
        )

        if success:
            return Response(
                {"message": message},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error": message},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def destroy(self, request, pk=None):
        try:
            # Fetch the object with the provided primary key (pk)
            obj = Favorite.objects.get(pk=pk)
        except Favorite.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()        
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecommendationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        recommendations = LibraryService.get_recommended_books(request.user)
        serializer = BookSerializer(recommendations, many=True)
        return Response(serializer.data)

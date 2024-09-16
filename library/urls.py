from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.views import (
    AuthorViewSet,
    BookViewSet,
    FavoriteViewSet,
    RecommendationViewSet,
)


router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('books', BookViewSet, basename='books')
router.register('favorites', FavoriteViewSet, basename='favorites')
router.register('recommendations', RecommendationViewSet, basename='recommendations')

urlpatterns = [
    path('', include(router.urls)),
]

import re
import uuid
from django.db.models import Q

from library.models import Book, Favorite
from accounts.models import CustomUser


class LibraryService:
    @staticmethod
    def add_to_favorites(user: CustomUser, book_id: uuid.UUID) -> bool:
        # Step 1: Check if the user already has 20 favorite books
        if Favorite.objects.filter(user=user).count() >= 20:
            return False, "You cannot have more than 20 favorite books."

        # Step 2: Add the book to the user's favorites
        try:
            book = Book.objects.get(id=book_id)
            Favorite.objects.create(user=user, book=book)
            return True, "Book added to favorites."
        except Book.DoesNotExist:
            return False, "Book not found."
        except Exception as e:
            print(f"Error adding to favorites: {e}")
            return False, "An error occurred."

    @staticmethod
    def get_recommended_books(user: CustomUser):
        # Step 1: Retrieve favorite books' titles
        favorite_books = Favorite.objects.filter(user=user).values_list('book__title', flat=True)
        if not favorite_books:
            # No recommendations if no favorites
            return Book.objects.none()

        # Step 2: Build a Q object to search for each word in the titles
        search_query = Q()
        for favorite_title in favorite_books:
            # Extract individual words from the title
            words = re.findall(r'\b\w+\b', favorite_title.lower())
            for word in words:
                # Add a search condition for each word
                search_query |= Q(title__icontains=word)

        # Step 3: Filter books that match the search query and exclude favorites
        books = Book.objects.exclude(favorited_by__user=user).filter(search_query).distinct()[:5]

        return books

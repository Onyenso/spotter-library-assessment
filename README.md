# Django Library API with JWT Authentication

This is a Django-based RESTful API that manages books, authors, and user favorites. The API uses **Django Rest Framework (DRF)** and **JWT authentication** for secure user authentication. Users can search for books, manage their favorite books, and receive book recommendations based on their favorites. The project is divided into two main apps: `accounts` for user management and authentication, and `library` for managing books, authors, and favorites.

## Features

- **User Registration and Authentication**: JWT-based authentication system with user registration and login endpoints.
- **Books & Authors Management**: Create, update, and delete books and authors (protected endpoints).
- **Favorites System**: Users can add or remove books from their favorites list (max 20 favorites).
- **Book Recommendations**: Recommendations are provided based on favorite book titles.
- **Search Functionality**: Search books by title or author name.
- **Permissions**: Only the creator of a book, author, or favorite can update or delete it.

## Tech Stack

- Python 3.8+
- Django 4.x
- Django Rest Framework
- PostgreSQL (for full-text search)
- Simple JWT for authentication

## Endpoints

1. **Authentication**: JWT for user authentication with registration (`POST /register`) and login (`POST /login`).
2. **Book and Author Management**:
    - `GET /books/`: Retrieve all books.
    - `GET /books/:id`: Retrieve a book by ID.
    - `POST /books/`: Create a new book (protected).
    - `PUT /books/:id`: Update a book (protected, owner only).
    - `DELETE /books/:id`: Delete a book (protected, owner only).
    - Similar endpoints exist for managing authors.
3. **Favorites**:
    - `GET /favorites/`: Retrieve a user's favorite books.
    - `POST /favorites/`: Add a book to the favorites list (max 20).
    - `GET /recommendations` Get suggested books based on favorites.
4. **Search**:
  - `GET /books?search=<query>`: Search for books by title or author.

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Pipenv or virtualenv

### Clone the repository

```
# bash
git clone https://github.com/Onyenso/spotter-library-assessment.git
cd spotter-library-assesment
```
### Create and activate a virtual environment

```
# Using pipenv
pipenv shell

# Or using virtualenv
python3 -m venv venv
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```

### Setup environment variables
Create a .env file in the root of your project and configure your database:

```
DJANGO_SETTINGS_MODULE="config.settings.development"
SECRET_KEY=
DATABASE_URL=
```

### Apply migrations
```
python manage.py migrate
```

### Run server
```
python manage.py runserver
```

### Live App
- https://spotter-library-production.up.railway.app










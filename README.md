# Boardgame World

Boardgame World is a small Django web application for cataloging board games, writing reviews, and organizing games into curated collections.

The project was created as a study project for practicing Django models, views, forms, templates, and PostgreSQL integration.  
The idea comes from a personal interest in board games and the desire to build a simple place where games can be stored, explored, and reviewed.

## Features

- Home page with latest games and featured collections
- Full CRUD for games
- Full CRUD for reviews
- Collections list and collection details
- Multiple genres per game
- Filtering games by genre and player count
- Sorting games by title or duration
- Custom 404 page
- Reusable partial templates and shared base layout

## Project structure

The project contains three Django apps:

- `games` — game catalog, game details, genres, create/edit/delete pages
- `games_collections` — curated game collections
- `reviews` — review list, create/edit/delete review pages

## Models and relationships

- `Game`
- `Collection`
- `Review`

Relationships:
- One `Game` can have many `Review` objects
- One `Collection` can contain many `Game` objects
- One `Game` can belong to many `Collection` objects

## Tech stack

- Python
- Django
- PostgreSQL
- Bootstrap 5
- django-unfold

## Environment variables

Normally sensitive configuration should not be stored in a repository.  
However, for the purposes of this university project a `.env` file is included intentionally.

This allows the project to be downloaded and run immediately without additional configuration, making the evaluation process easier.

The `.env` file contains only local database settings used for development.

---

## Running the project

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run migrations
5. Start the development server

Example:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open in the browser:
```http://127.0.0.1:8000/```

---

## Pages

The application contains multiple dynamic pages including:

- Home page
- Games list
- Game details
- Create/Edit/Delete game
- Genre pages
- Collections list and detail pages
- Reviews list
- Create/Edit/Delete review
- Custom 404 page

---

## Notes

Authentication is intentionally not implemented because it is outside the scope of the assignment requirements.

The project focuses on Django architecture, database relationships, forms, and template rendering.

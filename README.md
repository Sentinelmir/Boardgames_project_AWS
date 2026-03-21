# Boardgame World

Boardgame World is a Django web application for cataloging board games, writing reviews, and organizing them into collections.

You can view the live project here:
👉 http://13.50.157.69/

## Features

- Game catalog with full CRUD functionality
- Reviews system (create, edit, delete)
- Collections of games
- Filtering by genre and player count
- Sorting by title and duration
- Custom 404 page

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

---

## Running the project

Environment variables are not included in the repository.

To run the project locally, create your own .env file with the required settings, then:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open in the browser:
```http://127.0.0.1:8000/```

---

## Notes

This project was built for learning purposes, focusing on Django architecture, database relationships, and server deployment.

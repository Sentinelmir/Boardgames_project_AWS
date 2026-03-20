from django.db import migrations


GAMES_DATA = [
    {
        "title": "Brass: Birmingham",
        "slug": "brass-birmingham",
        "description": "An economic strategy game about building industries, developing networks, and managing resources during the Industrial Revolution.",
        "genres": ["economic", "strategy"],
        "min_players": 2,
        "max_players": 4,
        "duration_min": 120,
        "age_min": 14,
        "image": "games/brass-birmingham.jpg",
    },
    {
        "title": "Terraforming Mars",
        "slug": "terraforming-mars",
        "description": "Players manage corporations, develop projects, and compete to make Mars habitable while building an efficient engine.",
        "genres": ["economic", "strategy", "thematic"],
        "min_players": 1,
        "max_players": 5,
        "duration_min": 120,
        "age_min": 12,
        "image": "games/terraforming-mars.jpg",
    },
    {
        "title": "Root",
        "slug": "root",
        "description": "An asymmetric strategy game where woodland factions battle for control using completely different play styles.",
        "genres": ["strategy", "thematic"],
        "min_players": 2,
        "max_players": 4,
        "duration_min": 90,
        "age_min": 10,
        "image": "games/root.jpg",
    },
    {
        "title": "Wingspan",
        "slug": "wingspan",
        "description": "A strategy game about attracting birds to wildlife preserves and building a strong engine across several habitats.",
        "genres": ["family", "strategy"],
        "min_players": 1,
        "max_players": 5,
        "duration_min": 70,
        "age_min": 10,
        "image": "games/wingspan.jpg",
    },
    {
        "title": "Azul",
        "slug": "azul",
        "description": "An abstract strategy game where players draft colorful tiles and place them carefully to score points efficiently.",
        "genres": ["abstract", "family", "strategy"],
        "min_players": 2,
        "max_players": 4,
        "duration_min": 40,
        "age_min": 8,
        "image": "games/azul.jpg",
    },
    {
        "title": "Pandemic",
        "slug": "pandemic",
        "description": "A cooperative game where players work together as specialists trying to stop disease outbreaks around the world.",
        "genres": ["cooperative", "strategy", "thematic"],
        "min_players": 2,
        "max_players": 4,
        "duration_min": 45,
        "age_min": 8,
        "image": "games/pandemic.jpg",
    },

{
    "title": "Viticulture",
    "slug": "viticulture",
    "description": "A worker-placement game about building a successful winery, managing seasons, fulfilling wine orders, and developing long-term production.",
    "genres": ["economic", "strategy"],
    "min_players": 1,
    "max_players": 6,
    "duration_min": 90,
    "age_min": 13,
    "image": "games/viticulture.jpg",
},
{
    "title": "Dune: Imperium",
    "slug": "dune-imperium",
    "description": "A strategic blend of deck-building and worker placement where players compete for influence, alliances, and military control on Arrakis.",
    "genres": ["strategy", "thematic"],
    "min_players": 1,
    "max_players": 4,
    "duration_min": 120,
    "age_min": 13,
    "image": "games/dune-imperium.jpg",
},
{
    "title": "Blood Rage",
    "slug": "blood-rage",
    "description": "A highly confrontational miniatures game where Viking clans battle, upgrade warriors, complete quests, and seek glory before Ragnarok.",
    "genres": ["strategy", "thematic"],
    "min_players": 2,
    "max_players": 4,
    "duration_min": 90,
    "age_min": 14,
    "image": "games/blood-rage.jpg",
},
{
    "title": "Gloomhaven",
    "slug": "gloomhaven",
    "description": "A large cooperative campaign game with tactical combat, character progression, branching scenarios, and persistent world changes.",
    "genres": ["cooperative", "strategy", "thematic"],
    "min_players": 1,
    "max_players": 4,
    "duration_min": 120,
    "age_min": 14,
    "image": "games/gloomhaven.jpg",
},
]


COLLECTIONS_DATA = [
    {
        "title": "Economic Favorites",
        "slug": "economic-favorites",
        "description": "Games focused on planning, efficiency, and long-term decisions.",
        "games": ["brass-birmingham", "terraforming-mars", "viticulture"],
    },
    {
        "title": "Strategy Essentials",
        "slug": "strategy-essentials",
        "description": "Strong strategy titles for players who enjoy meaningful choices.",
        "games": [
            "brass-birmingham",
            "terraforming-mars",
            "root",
            "wingspan",
            "azul",
            "pandemic",
            "viticulture",
            "dune-imperium",
            "blood-rage",
            "gloomhaven",
        ],
    },
    {
        "title": "Accessible Game Night",
        "slug": "accessible-game-night",
        "description": "Games that are easy to bring to the table and still stay interesting.",
        "games": ["wingspan", "azul", "pandemic", "viticulture"],
    },
    {
        "title": "Epic Thematic Games",
        "slug": "epic-thematic-games",
        "description": "Large-scale games with strong atmosphere, conflict, and memorable sessions.",
        "games": ["dune-imperium", "blood-rage", "gloomhaven", "root"],
    },
]

REVIEWS_DATA = [
    {
        "game_slug": "brass-birmingham",
        "author_name": "Elena",
        "rating": 5,
        "text": "Deep economic gameplay with satisfying long-term planning.",
    },
    {
        "game_slug": "terraforming-mars",
        "author_name": "Nikolay",
        "rating": 5,
        "text": "A great engine-building game with lots of replayability.",
    },
    {
        "game_slug": "root",
        "author_name": "Ira",
        "rating": 4,
        "text": "Very thematic and clever, especially once everyone knows the factions.",
    },
    {
        "game_slug": "wingspan",
        "author_name": "Mira",
        "rating": 5,
        "text": "Beautiful presentation and smooth strategic decisions.",
    },
    {
        "game_slug": "azul",
        "author_name": "Pavel",
        "rating": 4,
        "text": "Simple rules, but the drafting decisions are excellent.",
    },
    {
        "game_slug": "pandemic",
        "author_name": "Anna",
        "rating": 5,
        "text": "A tense cooperative game that works very well with new players.",
    },
{
    "game_slug": "viticulture",
    "author_name": "Sofia",
    "rating": 5,
    "text": "A very satisfying worker-placement game with a cozy theme and strong planning.",
},
{
    "game_slug": "dune-imperium",
    "author_name": "Maksim",
    "rating": 5,
    "text": "Excellent combination of deck-building and worker placement with real tension.",
},
{
    "game_slug": "blood-rage",
    "author_name": "Artem",
    "rating": 4,
    "text": "Fast, aggressive, and dramatic. Great for players who enjoy direct conflict.",
},
{
    "game_slug": "gloomhaven",
    "author_name": "Olga",
    "rating": 5,
    "text": "Huge campaign depth and very strong tactical combat if you want a long-term game.",
},
]


def seed_initial_data(apps, schema_editor):
    Game = apps.get_model("games", "Game")
    Collection = apps.get_model("games_collections", "Collection")
    Review = apps.get_model("reviews", "Review")

    created_games = {}

    for game_data in GAMES_DATA:
        game, _ = Game.objects.update_or_create(
            title=game_data["title"],
            defaults={
                "slug": game_data["slug"],
                "description": game_data["description"],
                "genres": game_data["genres"],
                "min_players": game_data["min_players"],
                "max_players": game_data["max_players"],
                "duration_min": game_data["duration_min"],
                "age_min": game_data["age_min"],
                "image": game_data["image"],
            },
        )
        created_games[game.slug] = game

    for collection_data in COLLECTIONS_DATA:
        game_slugs = collection_data["games"]

        collection, _ = Collection.objects.update_or_create(
            title=collection_data["title"],
            defaults={
                "slug": collection_data["slug"],
                "description": collection_data["description"],
            },
        )

        collection.games.set(
            [created_games[slug] for slug in game_slugs if slug in created_games]
        )

    for review_data in REVIEWS_DATA:
        game = created_games.get(review_data["game_slug"])
        if not game:
            continue

        Review.objects.update_or_create(
            game=game,
            author_name=review_data["author_name"],
            defaults={
                "rating": review_data["rating"],
                "text": review_data["text"],
            },
        )


def remove_seed_initial_data(apps, schema_editor):
    Game = apps.get_model("games", "Game")
    Collection = apps.get_model("games_collections", "Collection")
    Review = apps.get_model("reviews", "Review")

    review_pairs = [(item["game_slug"], item["author_name"]) for item in REVIEWS_DATA]
    for game_slug, author_name in review_pairs:
        Review.objects.filter(
            game__slug=game_slug,
            author_name=author_name,
        ).delete()

    Collection.objects.filter(
        slug__in=[item["slug"] for item in COLLECTIONS_DATA]
    ).delete()

    Game.objects.filter(
        slug__in=[item["slug"] for item in GAMES_DATA]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
        ("games_collections", "0001_initial"),
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_initial_data, remove_seed_initial_data),
    ]
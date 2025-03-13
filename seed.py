from datetime import date
from app import app
from app import db 
from app.models import Book  

def seed_data():
    """Populate the database with sample book data."""
    books_data = [
        {
            "name": "Inception: The Shooting Script",
            "publish_date": date(2010, 7, 16),
            "add_to_site_at": date(2024, 3, 8),
            "description": "Inception, writer-director Christopher Nolan’s seventh feature film...",
            "image_url": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1582238792i/8565270.jpg",
            "author_id": 1,
            "price": 19.99,
            "appropriate": "adults"
        },
        {
            "name": "Who Is Lionel Messi?",
            "publish_date": date(2020, 1, 1),
            "add_to_site_at": date(2024, 3, 8),
            "description": "Lionel Messi loved soccer from an early age...",
            "image_url": "https://m.media-amazon.com/images/I/81+PPW+xJ7L._SY425_.jpg",
            "author_id": 2,
            "price": 9.99,
            "appropriate": "8-15"
        },
        {
            "name": "Darkly Dreaming Dexter",
            "publish_date": date(2004, 7, 1),
            "add_to_site_at": date(2024, 3, 8),
            "description": "Meet Dexter Morgan, a polite wolf in sheep's clothing...",
            "image_url": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1557598685i/17231.jpg",
            "author_id": 3,
            "price": 14.99,
            "appropriate": "adults"
        },
        {
            "name": "The Punisher",
            "publish_date": date(2022, 1, 1),
            "add_to_site_at": date(2024, 3, 8),
            "description": "The Punisher story to end all Punisher stories...",
            "image_url": "https://cdn.marvel.com/u/prod/marvel/i/mg/4/60/63876f478ff02/clean.jpg",
            "author_id": 4,
            "price": 12.99,
            "appropriate": "adults"
        },
        {
            "name": "Forrest Gump",
            "publish_date": date(1986, 9, 1),
            "add_to_site_at": date(2024, 3, 8),
            "description": "Meet Forrest Gump, the lovable, herculean, and surprisingly savvy hero...",
            "image_url": "https://m.media-amazon.com/images/I/71xzEu8NuJL._AC_UF1000,1000_QL80_.jpg",
            "author_id": 5,
            "price": 10.99,
            "appropriate": "adults"
        },
    ]

    with app.app_context():  # Ensure we're in the Flask app context
        db.create_all()  # Create tables if they don't exist
        db.session.bulk_insert_mappings(Book, books_data)  # Efficient bulk insert
        db.session.commit()
        print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_data()

from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    books = db.relationship('Book', backref='author', lazy=True)  

    def __repr__(self):
        return f"<Author {self.name}>"
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    add_to_site_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    appropriate = db.Column(db.Enum("under 8", "8-15", "adults", name="age_group"), nullable=False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Book {self.name} - {self.author.name}>"

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), default='user')  

    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

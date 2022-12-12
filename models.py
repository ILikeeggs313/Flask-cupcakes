"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
DEF_IMG = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """cupcakes"""
    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key = True,
    autoincrement = True)

    flavor = db.Column(db.String(100), nullable = False)
    size = db.Column(db.String(100), nullable = False)
    rating = db.Column(db.Float, nullable = False)

    image = db.Column(db.Text, nullable = False, default = DEF_IMG)

def connect_db(app):
    """Connect app to database"""
    db.app = app
    db.init_app(app)


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):
class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String)
    title = db.Column(db.String(200))
    publisher = db.Column(db.String(100))
    date = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre = db.Column(db.String)
    description = db.Column(db.String)
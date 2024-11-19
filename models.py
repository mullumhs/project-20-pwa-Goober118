from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):
class Game(db.Model)
    id = db.Collumn(db.integer, primary_key = True)
    title = db. Collumn(db.string(200), Nullable = False)
    publisher = db.Collumn(db.string(100), Nullable = True)
    rating = db.Collumn(db.float, Nullable = True)
    genre = db.Collumn(db.string, Nullable = True)
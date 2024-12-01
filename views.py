from flask import render_template, request, redirect, url_for, flash
from models import db, Game # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def index():
        # This route should retrieve all items from the database and display them on the page.
        games = Game.query.all()
        return render_template('index.html', games = games) 



    @app.route('/add', methods=['GET', 'POST'])

    def add_item():

        if request.method == 'POST':

            # Handle form submission (POST request)

            # Extract item data from form
            title = request.form.get('title')
            publisher = request.form.get('publisher')
            date = request.form.get('date')
            rating = request.form.get('rating')
            genre = request.form.get('genre')
            description = request.form.get('description')
            # Add item to database
            new_item = Game(title = title, publisher = publisher, date = date, rating = rating, genre = genre, description = description)
            db.session.add(new_item)
            db.session.commit()
            # Redirect to a success page or item list

            return redirect(url_for('index'))

        else:

            # Display the add item form (GET request)
            
            return render_template('add_item.html')


    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')
from flask import render_template, request, redirect, url_for, flash
from models import db, Game 

def init_routes(app):

    # Route for the home page
    @app.route('/', methods=['GET'])
    def index():
        search_query = request.args.get('query')
        if search_query:
        # If there's a search query, filter the results
            games = Game.query.filter(Game.title.ilike(f'%{search_query}%')).all()
        else:
        # If no search query, return all items
            games = Game.query.all()
        return render_template('index.html', games = games)

    # Route to add a new game
    @app.route('/add', methods=['GET', 'POST'])
    def add_item():
        if request.method == 'POST':
            # Extract item data from form
            image = request.form.get('image')
            title = request.form.get('title')
            publisher = request.form.get('publisher')
            date = request.form.get('date')
            rating = request.form.get('rating')
            genre = request.form.get('genre')
            description = request.form.get('description')
            # Create a new game object and add it to the database
            new_item = Game(image = image, title = title, publisher = publisher, date = date, rating = rating, genre = genre, description = description)
            db.session.add(new_item)
            db.session.commit()

            # Redirect to the homepage after adding the game
            return redirect(url_for('index'))

        else:
            return render_template('add_item.html')

    # Route to edit an existing game
    @app.route('/edit', methods=['GET', 'POST'])
    def edit_item():

        if request.method == 'POST':
            id = request.form.get('id')
            game = Game.query.get(id)

            # Extract item data from form
            game.image = request.form.get('image')
            game.title = request.form.get('title')
            game.publisher = request.form.get('publisher')
            game.date = request.form.get('date')
            game.rating = request.form.get('rating')
            game.genre = request.form.get('genre')
            game.description = request.form.get('description')
            
            # Commit the changes to the database
            db.session.commit()
            
            # Redirect to the home pagr
            return redirect(url_for('index'))

        else:

            # Display the add item form (GET request)
            id = request.args.get('id')
            game = Game.query.get(id)
            return render_template('edit_item.html', game = game)

    # Route to delete a game
    @app.route('/delete', methods=['GET'])
    def delete_item():
        # Get the id of the game to delete, retrieve and then delete from the database
        id = request.args.get('id')
        game = Game.query.get(id)
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('index'))

    # Route to view the details of a single game
    @app.route('/view', methods=['GET'])
    def view_item():
        id = request.args.get('id')
        game = Game.query.get(id)
        return render_template('view_item.html', game = game)
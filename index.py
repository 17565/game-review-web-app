""" this is  the main set of code form my web app"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'

db = SQLAlchemy(app)

#game table
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(50))
    image = db.Column(db.String(50))
    release_date = db.Column(db.String(50))
    gener_id = db.Column(db.Integer, db.ForeignKey('gener.id'),
        nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'),
        nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'),
        nullable=False)

    reviews = db.relationship('Review', backref='game', lazy=True)

#review table
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(50))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'),
        nullable=False)

# gener table
class Gener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gener = db.Column(db.String(50))

    games = db.relationship('Game', backref='gener', lazy=True)

#publisher table
class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(50))

    publisher_id = db.relationship('Game', backref='Publisher', lazy=True)

#developer table
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    developer = db.Column(db.String(50))

    developer_id = db.relationship('Game', backref='Developer', lazy=True)

# @app.route()
@app.route("/games")
def games():
    results = Game.query.all()
    return render_template("my_games.html" , results=results)

#displays page
@app.route("/")
def home():
    return render_template ("home_page.html")

#displays page
@app.route("/add", methods=["POST", "GET"])
def add_review():
    if request.method == "POST":
        new_review = Review()
        new_review.game_id = request.form.get('game')
        new_review.review = request.form.get('review')
        db.session.add(new_review)
        db.session.commit()
        return redirect('/add')
    games = Game.query.all()
    return render_template ("add_review.html", games=games)

@app.route("/individuals/<int:id>")
def individuals(id):
    game = Game.query.filter_by(id = id).first()
    gener = Gener.query.filter_by(id=game.gener_id).first()
    publisher = Publisher.query.filter_by(id=game.publisher_id).first()
    developer = Developer.query.filter_by(id=game.developer_id).first()
    return render_template("individual_game_page.html" , game=game,gener=gener,publisher=publisher,developer=developer)

#runs app
if __name__ == "__main__":
    app.run(debug=True)
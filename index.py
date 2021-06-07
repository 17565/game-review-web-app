""" this is  the main set of code form my web app"""

from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'

db = SQLAlchemy(app)
#game table
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(50))
    reviews = db.relationship('Review', backref='game', lazy=True)
    image = db.Column(db.String(50))
#    release_date = db.Column(db.String(50))
#    gener_id = db.Column(db.Integer, db.ForeignKey(''),
#        nullable=False)
#    publisher_id = db.Column(db.Integer, db.ForeignKey(''),
#        nullable=False)
#    developer_id = db.Column(db.Integer, db.ForeignKey(''),
#        nullable=False)
#review table
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(50))
#    release_date = db.Column(db.DateTime, default=datetime.now)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'),
        nullable=False)

    
@app.route("/games")
def Index():
    results = Game.query.all()
    return render_template("my_games.html" , results=results)

#displays page
@app.route("/")
def games():
    return render_template ("home_page.html")

#runs app
if __name__ == "__main__":
    app.run(debug=True)

"""gener table
class Gener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gener = db.Column(db.string(50))
#publisher table
class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.string(50))
#developer table
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    developer = db.Column(db.string(50))"""
""" this is  the main set of code form my web app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.games'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.column(db.integer, primary_key=True)
    game = db.column(db.string(50))
    image = db.Column(db.String(50))
    gener_id = db.Column(db.String(50))
    release_date = db.Column(db.String(50))
    publisher = db.Column(db.String(50))
    developer = db.Column(db.String(50))


    
@app.route("/")
def Index():
    return "<h1>hello world<?h1>"

#runs app
if __name__ == "__main__":
    app.run(debug=True)
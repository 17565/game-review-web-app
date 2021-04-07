""" this is  the main set of code form my web app"""
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.games'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(50))
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

#>>> from test_code import db
#>>> db.create_all()

#>>> from test_code import User
#>>> bob = User(name = "starcraft")
#>>> db.session.add(bob)
#>>> db.session.commit()
#>>> from test_code import db,User
#>>> sc = User.query.filter_by(id = 1).first()
#>>> sc
#<User 1>

#>>> sc = User.query.filter_by(id = 2).first()
#>>> db.session.delete(sc)     
#>>> db.session.commit()
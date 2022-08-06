from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))



    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return "<User %r>" % self.username


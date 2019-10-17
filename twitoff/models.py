"""SQLAlchemy models for Twitoff
Create one for data, and one for users,
each with a separate table."""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we pull and analyze"""
    id = DB.Column(DB.Integer, primary_key=True) # autogenerates IDs
    name = DB.Column(DB.String(15), unique=True, nullable=False)
    followers = DB.Column(DB.BigInteger)  # , nullable=False
    #Tweets IDs are ordinal ints, so we can fetch
    newest_tweet_id = DB.Column(DB.BigInteger, nullable=False)

    def __repre__(self):
        return '<User {}>'.format(self.name)

class Tweets(DB.Model):
    """Stores tweets """
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280)) #unicode allows emojis, + than just string
    embedding = DB.Column(DB.PickleType, nullable=False)

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)

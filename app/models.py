"""
Notes to self:
- Data in database is represented by a collection of classes (database models)
- The ORM links Python to the relationship database by mapping relational bits to object graphs

Primary key: ID field, which is in all models
- User in the database is assigned a unique ID value stored in ID field
- Primary keys are automatically assigned

Other fields:
- username, email, and password_hash (strings or VARCHAR with max lengths)
- user passwords are not stored in the database, password hashes are instored instead
- lengths minimized (specified) to database can optimize space usage

Resources:
- WWW Designer Tool: https://ondras.zarovi.cz/sql/demo/

Pseudo Code Description:
- User class inherits from db.Model (base class for all models from FlaskSQLAlchemy
- User class defines fields as variables, which are instances of db.Column class
    - takes field type as an argument + other optional arguments
- __repr__ tells Python how to print objects of this class, which is useful for debugging.

Initialized database: flask db init
Migrate database: flask db migrate
Apply changes: flask db upgrade
Reverse changes: flask db downgrade

"""
from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', brackref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {} Email {}>'.format(self.username, self.email)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
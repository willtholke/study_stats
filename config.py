""" Configuration settings are defined as class variables inside
the Config class. It's good practice to set configuration from
environment variables and provide a fallback value when the
environment does not define the variable.

SECRET_KEY = cryptographic key
Used with Flask-WTF extension to protect web forms against CSRF

"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # dict of environ variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')  # try to get database URL or make database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # disable feature

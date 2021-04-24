""" Configuration settings are defined as class variables inside
the Config class.

SECRET_KEY = cryptographic key
Used with Flask-WTF extension to protect web forms against CSRF

"""
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

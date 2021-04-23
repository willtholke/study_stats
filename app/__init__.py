""" This file will execute when the app package is imported and
defines what symbols the package exposes.

App package is defined by the app directory and __init__.py script
while the app variable is an instance of class Flask.

The routes module is imported at the bottom to work around circular
imports. Routes module needs to import the app varibale,
so putting the import at the bottom avoids the arror that results
from mutual references between the two files.
"""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

""" Configuration settings are defined as class variables inside
the Config class.
"""
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

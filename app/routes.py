""" Handlers for the application routes are written as
view functions.

@app.route is a decorator that creates an association between
the URL given as an argument and the function.

When a web browser requests either of these two URLS, Flask invokes
the function and passes the return value back to the browser.

Rendering converts a template into a complete HTML page using Jinja2.



"""
from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    """ Take a template filename and variable list of template
    arguments and return the same template but with
    placeholders in it replaced with real values. """
    user = {'username': 'Will'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Los Altos!'
        },
        {
            'author': {'username': 'Will'},
            'body': 'Testing; one, two.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign in", form=form)
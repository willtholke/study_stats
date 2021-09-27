# Study Stats Project [Deprecated]

## Navigation
1) [Running the Application](#running-the-application)
1) [Personal Notes](#personal-notes)
2) [Objectives](#objectives)
2) [Resources](#resources)

## Personal Notes
SQLAlchemy follows the relational model in that SQL (a popular relational
query language) is implemented. I'm using a SQLite database in development
sinch each database is stored in a single file and
there is no use for a database server. These configs are added
in the config.py file.

## Structure
```
study-stats/
  venv/
  app/
    __init__.py
    routes.py
    templates/
      base.html
      index.html
  app.py
  config.py
```

## Running the application
1) Set the `FLASK_APP` environment
```
venv() $ export FLASK_APP=app.py
```
```
source venv/bin/activate
```
This tells Flask how to import the web application.

2) Run the application
```
(venv) $ flask run
```

3) Install the python-dotenv package to register environment
variables to be automatically imported when running the `flask` command.
```
(venv) $ pip install python-dotenv
```   
The /.flaskenv file holds this!

4) Install Flask-SQLAlchemy in your virtual environment after it's activated
```
(venv) $ pip install flask-sqlalchemy
```

5) To work with database migrations, install `flask-migrate`
```
(venv) $ pip install flask-migrate
```

## Resources
- [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Flask Docs: Larger Application Design](https://flask.palletsprojects.com/en/1.1.x/patterns/packages/)
- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/api/#)

## Objectives
- Implement database in SQLAlchemy
- OAuth, styling, timer functionality

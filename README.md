# Study Stats Project

## Resources
[The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Structure
```
study-stats/
  venv/
  app/
    templates/
      index.html
    __init__.py
    routes.py
  app.py
```

## Running the application
1) Set the `FLASK_APP` environment
```
venv() $ export FLASK_APP=app.py
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
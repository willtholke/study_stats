# Study Stats Project

## Resources
- [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Flask Docs: Larger Application Design](https://flask.palletsprojects.com/en/1.1.x/patterns/packages/)
- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/api/#)


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
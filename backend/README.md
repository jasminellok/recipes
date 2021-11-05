# Recipe Book API

The backend Flask server provides the frontend webapp with an API to access/modify recipes saved in the database.

## Dependencies

- `pip install Flask`
- `pip install python-dotenv`
- `pip install psycopg2`
- `pip install flask-cors`


## Running the Flask Server

You will need to set `pg_password` in a .env file in the backend directory.

Command to start the server: `FLASK_APP=backend/server.py flask run`

## Units Tests

This uses the built in 'unittest' module. Automatically discover and run tests matching 'test*.py' with this command (must be in 'backend' directory): `python -m unittest discover`
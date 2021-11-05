from model.ingredient import Ingredient
from model.recipe import Recipe
from model.step import Step
import json
import psycopg2
from psycopg2 import pool
import os
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

pg_pool = psycopg2.pool.ThreadedConnectionPool(2,  # min connections
                                               10,  # max connections
                                               host='localhost',
                                               port=5432,
                                               database='recipe_book',
                                               user='postgres',
                                               password=os.environ.get('pg_password'))

app = Flask(__name__)
cors = CORS(app)  # enables CORS on app


@app.route('/')  # defining url path for server to respond to... http request
def hello_world():
    return 'Recipe-Book API is up'


@app.route('/recipes')  # website .../ recipes
def query_recipes():
    connection = pg_pool.getconn()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM recipes;')
    rows = cursor.fetchall()
    recipes = [Recipe.from_row(row) for row in rows]
    pg_pool.putconn(connection)
    return json.dumps(recipes, default=lambda x: x.__dict__)


@app.route('/recipe/<recipe_id>')
def query_recipe(recipe_id):
    connection = pg_pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM recipes WHERE id = %(id)s;',
        {
            'id': recipe_id
        })
    row = cursor.fetchone()
    recipe = Recipe.from_row(row)
    pg_pool.putconn(connection)
    return json.dumps(recipe, default=lambda x: x.__dict__)


@app.route('/recipe', methods=["POST"])
def new_recipe():
    # TODO validate recipe, ingredients, and steps before attempting to insert
    recipe_id = add_recipe(request.json['recipe'])
    print('added recipe ID: {}'.format(recipe_id))
    add_ingredients(recipe_id, request.json['ingredients'])
    add_steps(recipe_id, request.json['steps'])
    return 'OK' # TODO return ERROR if something went wrong


@app.route('/ingredients/<recipe_id>')
def query_ingredients(recipe_id):
    connection = pg_pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM ingredients WHERE recipe_id = %(recipe_id)s',
        {
            'recipe_id': recipe_id
        })
    rows = cursor.fetchall()
    ingredients = [Ingredient.from_row(row) for row in rows]
    pg_pool.putconn(connection)
    return json.dumps(ingredients, default=lambda x: x.__dict__)


@app.route('/steps/<recipe_id>')
def query_steps(recipe_id):
    connection = pg_pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM steps WHERE recipe_id = %(recipe_id)s',
        {
            'recipe_id': recipe_id
        })
    rows = cursor.fetchall()
    steps = [Step.from_row(row) for row in rows]
    pg_pool.putconn(connection)
    return json.dumps(steps, default=lambda x: x.__dict__)


def add_recipe(recipe):
    connection = pg_pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO recipes (title, description, author) \
        VALUES(%s, %s, %s) \
        RETURNING id;",
        (recipe['title'], recipe['description'], recipe['author']))
    recipe_id = cursor.fetchone()[0]
    connection.commit()
    pg_pool.putconn(connection)
    return recipe_id


def add_ingredients(recipe_id, ingredients):
    connection = pg_pool.getconn()
    cursor = connection.cursor()
    for ingredient in ingredients:
        cursor.execute(
            "INSERT INTO ingredients (recipe_id, name, amount, unit) \
            VALUES(%s, %s, %s, %s);",
            (recipe_id, ingredient['name'], ingredient['amount'], ingredient['unit']))
    connection.commit()
    pg_pool.putconn(connection)


def add_steps(recipe_id, steps):
    connection = pg_pool.getconn()
    cursor = connection.cursor()
    for step in steps:
        cursor.execute(
            "INSERT INTO steps (recipe_id, ordinal, instruction) \
            VALUES(%s, %s, %s);",
            (recipe_id, step['ordinal'], step['instruction']))
    connection.commit()
    pg_pool.putconn(connection)

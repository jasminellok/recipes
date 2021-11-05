import psycopg2
import os
from dotenv import load_dotenv

backend_dir = os.path.abspath('./backend')
dotenv_path = os.path.join(backend_dir, '.env')
print(dotenv_path)
load_dotenv(dotenv_path)

connection = psycopg2.connect(host='localhost',
                              database='recipe_book',
                              user='postgres',
                              password=os.environ.get('pg_password'))
cursor = connection.cursor()

"""
README
run from root level of project: python scripts/insert_db.py
make sure execution statement matches insert fields
"""

to_insert = \
[
    {
        'recipe_id': 7,
        'ordinal': 1,
        'instruction': 'place sausage in hotdog bun',
    },
    {
        'recipe_id': 7,
        'ordinal': 2,
        'instruction': 'apply ketchup and mustard onto sausage',
    },
]

for d in to_insert:
    cursor.execute("INSERT INTO steps (recipe_id, ordinal, instruction) VALUES(%s, %s, %s);",
                   (d['recipe_id'], d['ordinal'], d['instruction']))

connection.commit()

cursor.close()
connection.close()

"""
basic recipes
[
    {
        'title': 'cake',
        'description': 'yummy cake',
        'author': 'jazzybutt'
    },
    {
        'title': 'hotto doggu',
        'description': 'weiner and bun',
        'author': 'doge'
    },
]

hot dog ingredients
[
    {
        'recipe_id': 7,
        'name': 'sausage',
        'amount': '1',
        'unit': None
    },
    {
        'recipe_id': 7,
        'name': 'hotdog bun',
        'amount': '1',
        'unit': None
    },
    {
        'recipe_id': 7,
        'name': 'mustard',
        'amount': '1',
        'unit': 'tbs'
    },
    {
        'recipe_id': 7,
        'name': 'ketchup',
        'amount': '1',
        'unit': 'tbs'
    },
]
"""

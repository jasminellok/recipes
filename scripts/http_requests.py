'''
A script to use as a Postman/Insomnia stand-in. Requires the requests module.

pip install requests
'''


import requests

req_body = {}

recipe = {
  'title': 'beans',
  'author': 'memes',
  'description': 'why are there so many beans memes'
}
ingredients = [
  {
    'name': 'pinto beans',
    'amount': 1.0,
    'unit': 'cup'
  },
  {
    'name': 'water',
    'amount': 2.0,
    'unit': 'cups'
  }
]
steps = [
  {
    'ordinal': 1,
    'instruction': 'put water and beans in a pot'
  },
  {
    'ordinal': 2,
    'instruction': 'boil until beans are tender'
  }
]

req_body['recipe'] = recipe
req_body['ingredients'] = ingredients
req_body['steps'] = steps

url = 'http://localhost:5000/recipe'
resp = requests.post(url, json = req_body)

print(resp.text)
import unittest
from recipe import Recipe
import json


class TestRecipe(unittest.TestCase):

    def test_row_to_object(self):
        row = (1, 'title', 'desc', 'author')

        recipe = Recipe.from_row(row)

        self.assertEqual(recipe.id, 1)
        self.assertEqual(recipe.title, 'title')
        self.assertEqual(recipe.description, 'desc')
        self.assertEqual(recipe.author, 'author')


if __name__ == '__main__':
    unittest.main()

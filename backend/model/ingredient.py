class Ingredient():
    def __init__(self, id, recipe_id, name, amount, unit):
        self.id = id
        self.recipe_id = recipe_id
        self.name = name
        self.amount = float(amount)
        self.unit = unit

    @classmethod
    def from_row(self, row):
        return self(id=row[0], recipe_id=row[1], name=row[2], amount=row[3], unit=row[4])

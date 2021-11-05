class Step():
    def __init__(self, id, recipe_id, ordinal, instruction):
        self.id = id
        self.recipe_id = recipe_id
        self.ordinal = ordinal
        self.instruction = instruction

    @classmethod
    def from_row(self, row):
        return self(id=row[0], recipe_id=row[1], ordinal=row[2], instruction=row[3])

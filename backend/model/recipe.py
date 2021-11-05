class Recipe():
    def __init__(self, id, title, description, author):
        self.id = id
        self.title = title
        self.description = description
        self.author = author

    @classmethod
    def from_row(self, row):
        return self(id=row[0], title=row[1], description=row[2], author=row[3])

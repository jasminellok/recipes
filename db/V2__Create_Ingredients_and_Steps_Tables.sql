ALTER TABLE recipes 
DROP COLUMN ingredients,
DROP COLUMN steps;

CREATE TABLE ingredients (
  id SERIAL PRIMARY KEY NOT NULL,
  recipe_id INTEGER REFERENCES recipes (id),
  name TEXT NOT NULL,
  amount DECIMAL NOT NULL,
  unit TEXT
);

CREATE TABLE steps (
  id SERIAL PRIMARY KEY NOT NULL,
  recipe_id INTEGER REFERENCES recipes (id),
  ordinal INTEGER NOT NULL,
  instruction TEXT NOT NULL
);
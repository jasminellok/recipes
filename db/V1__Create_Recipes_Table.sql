CREATE TABLE recipes (
  id SERIAL PRIMARY KEY NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  author TEXT NOT NULL,
  ingredients TEXT, -- set up real ingredients table later
  steps TEXT -- set up real steps table later
);

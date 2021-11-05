ALTER TABLE steps
DROP CONSTRAINT "steps_recipe_id_fkey",
ADD CONSTRAINT "steps_recipe_id_fkey"
  FOREIGN KEY ("recipe_id")
  REFERENCES "recipes" (id)
  ON DELETE CASCADE;

ALTER TABLE ingredients
DROP CONSTRAINT "ingredients_recipe_id_fkey",
ADD CONSTRAINT "ingredients_recipe_id_fkey"
  FOREIGN KEY ("recipe_id")
  REFERENCES "recipes" (id)
  ON DELETE CASCADE;
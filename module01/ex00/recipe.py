class book:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
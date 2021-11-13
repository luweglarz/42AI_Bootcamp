from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = str(name)
        self.last_update = datetime.now()
        self.creation_data = datetime.now()
        self.recipes_list = dict.fromkeys(['starter', 'lunch', 'dessert'])
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for i in self.recipes_list:
                if self.recipes_list[i] == name:
                    return self.recipes_list[i]
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for i in self.recipes_list:
            if i == recipe_type:
                print(i)
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        for i in self.recipes_list:
            if i == recipe.recipe_type:
                self.recipes_list[recipe.recipe_type] = recipe.name
                self.last_update = datetime.now()

            

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if name.isdigit() or name == "" :
            raise Exception("Error name")
        if cooking_lvl not in range(1, 5) or cooking_lvl == "":
            raise Exception("Error cooking_lvl")
        if recipe_type.isdigit() or recipe_type == "" :
            raise Exception("Error name")
        self.name = str(name)
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        if ingredients:
            self.ingredients = list(ingredients)
        else:
            raise Exception("Error ingredients")
        self.description = str(description)
        self.recipe_type = str(recipe_type)
    
    def __str__(self):
        text = "Recipe name: " + self.name + '\n'
        text += "Recipe level: " + str(self.cooking_lvl) + '\n'
        text += "Recipe time: " + str(self.cooking_time) + '\n'
        text += "Ingredients: " + '\n'
        for i in self.ingredients:
            text += i + '\n'
        text += "Recipe description: " + self.description + '\n'
        text += "Recipe type: " + self.recipe_type
        return text
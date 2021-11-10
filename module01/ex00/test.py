from book import Book
from recipe import Recipe

last_update = (2021, 1, 13, 8, 30)
creation_date = (2020, 4, 21, 10, 30)
recipes_list = {
    'starter',
    'lunch',
    'dessert',
}
ingredients = ['salad', 'cheese']

recipe_book = Book("Recipe book")
pizza = Recipe("pizza", 2, 30, ['olives', 'cheese', "meat"], "A yummy pizza", "lunch")
recipe_book.add_recipe(pizza)
recipe = recipe_book.get_recipe_by_name('pizza')

print("The added recipe:\n",recipe)
print(str(pizza))
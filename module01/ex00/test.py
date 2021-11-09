from book import Book
from recipe import Recipe

last_update = (2021, 1, 13, 8, 30)
creation_date = (2020, 4, 21, 10, 30)
recipes_list = {
    'starter',
    'lunch',
    'dessert',
}
recipes_list = dict.fromkeys(recipes_list)
ingredients = ['salad', 'cheese']
tourte = Recipe("tourte", 2, 30, ingredients, "une tourte", "lunch")
print(str(tourte))
san_ingredients = ['ham', 'bread', 'cheese', 'tomatoes']
c_ingredients = ['flour', 'sugar', 'egges']
sal_ingredients = ['avocado', 'aruyala', 'tomatoes', 'spinach']

cookbook = {
		'sandwich': {'ingredients': san_ingredients, 'meal': 'lunch', 'prep_time': '10mins'},
        'cake': {'ingredients': c_ingredients, 'meal': 'dessert', 'prep_time': '60mins'},
		'salad': {'ingredients': sal_ingredients, 'meal': 'lunch', 'prep_time': '15mins'}	
}

# for key in cookbook:
# 	print(key)

# for i in cookbook:
# 	for key in cookbook[i]:
#     		print(key)


# print(cookbook['sandwich']['ingredients'])

# for i in cookbook:
# 	for key in cookbook[i]:
# 		for item in cookbook[key]:
#     			print(item)

def	take_in():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit\n")
    return (input(">>>"))

def print_recipe(recipe):
    occurence = 0
    for i in cookbook:
        if i == recipe:
            occurence += 1
    if occurence == 0:
        return
    print("Recipe for", recipe)
    print("Ingrediens list:", cookbook[recipe]['ingredients'])
    print("To be eaten for", cookbook[recipe]['meal'])
    print("Takes", cookbook[recipe]['prep_time'], "of cooking\n")

def print_cookbook():
    print("All recipes:")
    for recipe in cookbook:
        print(recipe)
    print("")

def add_recipe(recipe, ingredients, meal, prep_time):
    i = 0
    while i < len(cookbook):
        i += 1
    cookbook[recipe] = { 'ingredients': list(ingredients.split(' ')),
    'meal' : meal, 'prep_time': prep_time}

def del_recipe(recipe):
    del cookbook[recipe]

def main():
    while 1:
        u_input = take_in()
        if (u_input == '1'):
            print("Please enter what recipe you want to add")
            recipe = input("Recipe: ")
            ingredients = input("Ingredients: ")
            meal = input("Meal: ")
            prep_time = input("Prep_time: ")
            add_recipe(recipe, ingredients, meal, prep_time)
        elif (u_input == '2'):
            print("Please enter what recipe you want to delete")
            recipe = input(">>>")
            del_recipe(recipe)
        elif (u_input == '3'):
            print("Please enter the recipe's name to get its details:")
            recipe = input(">>>")
            print_recipe(recipe)
        elif (u_input == '4'):
            print_cookbook()
        elif (u_input == '5'):
            return

if __name__ == "__main__":
    main()


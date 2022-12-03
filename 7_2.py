from pprint import pprint
recipes = []
recipes_count = 0
ingredients_counts = []


with open('sweets.txt', 'r') as ingredients_list:
    for line in ingredients_list:
        recipe_title = line.strip()
        recipe = {"recipe_title": recipe_title, "ingredients": []}
        ingredients_count = int(ingredients_list.readline())
        for i in range(int(ingredients_count)):
            ingr = ingredients_list.readline()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredient = {"ingredient_name": ingredient_name, "quantity": float(quantity), "measure": measure.strip()}
            recipe["ingredients"].append(ingredient)
        recipes.append(recipe)
        ingredients_list.readline()


def get_shop_list_by_dishes(dishes, person_count):
    ingr_dict_for_chef = {}

    for dish in dishes:
        for recipe in recipes:
            if recipe["recipe_title"] == dish:
                for k in range(int(ingredients_count)):
                    ingr_dict_for_chef.update({recipe["ingredients"][k]["ingredient_name"]:{"measure": recipe["ingredients"][k]["measure"], "quantity": recipe["ingredients"][k]["quantity"]*person_count}})
    pprint(ingr_dict_for_chef)



get_shop_list_by_dishes(['Fresh-sliced Oranges', 'Pavlova'], 10)


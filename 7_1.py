recipes = []
recipes_count = 0
ingredients_counts = []

with open('sweets.txt','r') as ingredients_list:
    for line in ingredients_list:
        recipe_title = line.strip()
        recipes_count += 1
        recipe = {"recipe_title": recipe_title, "ingredients": []}
        ingredients_count = int(ingredients_list.readline())
        ingredients_counts.append(ingredients_count)
        for i in range(int(ingredients_count)):
            ingr = ingredients_list.readline()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredient = {"ingredient_name": ingredient_name, "quantity": float(quantity), "measure": measure.strip()}
            recipe["ingredients"].append(ingredient)
        recipes.append(recipe)
        ingredients_list.readline()

print('cook_book={')
for recipe in recipes:
    print("'",recipe["recipe_title"],"':[")
    for i in range(len(recipe["ingredients"])):
        print(recipe["ingredients"][i])
print('}')











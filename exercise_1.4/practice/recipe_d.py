import pickle

recipe ={
    'name': 'tea',
    'ingredients': ['tea leaves', 'water', 'sigar'],
    'cooking_time_mins': 5,
    'difficulty': 'easy'
}

with open ('recipe_binary.bin', 'wb') as recipe_bin:
    pickle.dump(recipe, recipe_bin)

with open ('recipe_binary.bin', 'rb') as recipe:
    recipe = pickle.load(recipe)
    
print ('recipe_details: ')
print ('name: ' + recipe['name'])
print ('ingredients: ', recipe['ingredients'])
print('cooking_time_mins:', str(recipe['cooking_time_mins']))
print('difficulty: ' + recipe['difficulty'])
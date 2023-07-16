import pickle

recipes_list =[]
ingredients_list =[]

def take_recipe ():
    name = input('name of the recipe: ')
    cooking_time_minutes = int(input('cooking time: '))
    ingredients = []
    
    while True:
        an_ingredient = input('Please enter an ingredient or type "stop" to finish: ')
        if an_ingredient == 'stop':
           break
        ingredients.append(an_ingredient)

    recipe = {
        'name': name, 
        'cooking_time': cooking_time_minutes, 
        'ingredients': ingredients
    }
    return recipe

def get_difficulty(cooking_time_minutes, number_of_ingredients):

    if cooking_time_minutes < 10 and number_of_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time_minutes < 10 and number_of_ingredients >=4:
        difficulty = 'Medium'
    elif cooking_time_minutes >= 10 and number_of_ingredients <4:
        difficulty = 'Intermediate'
    elif cooking_time_minutes >=10 and number_of_ingredients >4:
        difficulty = 'Hard'
    
    return difficulty


#main code
filename = input ('enter the filename where you have stored your code: ')
try:
    with open(filename, 'rb'):
        data = pickle.load(recipes_list)
        print('loaded sucsesfully')
except FileNotFoundError:
    print ('this file does not exist. please create a new one')
    data = {'recipes_list':[], 'all_ingredients': []}
except:
    print('unexpexcted error occured')
    data = {'recipes_list':[], 'all_ingredients': []}
else:
    recipes_list.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


n = int(input('How many recipes would you like to enter: '))

for i in range (0 ,n):

    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    recipes_list.append(recipe)

    for recipe in recipes_list:

        print('')
        print(f'Name: {recipe["name"]}')
        print(f'Cooking time (mins): {recipe["cooking_time"]}')
        print('Ingredients')
        print('-----------')
        for ingredient in recipe['ingredients']:
            print(ingredient)

        difficulty = get_difficulty(recipe['cooking_time'], len(recipe['ingredients']))
        print(f'Difficulty: {difficulty}')



#print('')
#print('Ingredients Available Across All Recipes')
#print('----------------------------------------')
#for ingredient in sorted(ingredients_list):
    #print(ingredient)

data ={'recipes_list': recipes_list, 'ingredients_list':ingredients_list}

filename = input('Type the name of the file to store recipes: ')
with open(filename,'wb'):
   pickle.dump(data)
   print('saved successfully')
   
    
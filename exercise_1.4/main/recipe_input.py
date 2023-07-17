import pickle

recipes_list =[]
all_ingredients =[]

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
        'ingredients': ingredients,
        'difficulty': get_difficulty(cooking_time_minutes, len(ingredients))
    }
    return recipe

def get_difficulty(cooking_time_minutes, number_of_ingredients):

    if cooking_time_minutes < 10 and number_of_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time_minutes < 10 and number_of_ingredients >=4:
        difficulty = 'Medium'
    elif cooking_time_minutes >= 10 and number_of_ingredients <4:
        difficulty = 'Intermediate'
    elif cooking_time_minutes >=10 and number_of_ingredients >=4:
        difficulty = 'Hard'
    
    return difficulty


   # main code
if __name__ == '__main__':

    filename = input ('enter the filename where you have stored your code: ')
    try:
        # open a file defined by the path 'filename' and load the file object into a variable called 'file_stream'
        file_stream = open(filename, 'rb')
        data = pickle.load(file_stream)
        num_recipes = len(data['recipes_list'])
        print(f'loaded sucsesfully {num_recipes} recipes!')
    except FileNotFoundError:
        print('this file does not exist. It will be created at the end')
        data = {
            'recipes_list': [],
            'all_ingredients': []
        }
    except:
        print('unexpexcted error occured')
        data = {
            'recipes_list': [],
            'all_ingredients': []
        }
    else:
        file_stream.close()
    finally:
        recipes_list = data['recipes_list']
        all_ingredients = data['all_ingredients']
        all_ingredients = data["all_ingredients"]


    n = int(input('How many recipes would you like to enter: '))

for i in range (0 ,n):

    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    recipes_list.append(recipe)

   # for recipe in recipes_list:

       # print('')
        #print(f'Name: {recipe["name"]}')
        #print(f'Cooking time (mins): {recipe["cooking_time"]}')
        #print('Ingredients')
        #print('-----------')
        #for ingredient in recipe['ingredients']:
         #   print(ingredient)
         
         # difficulty = get_difficulty(recipe['cooking_time'], len(recipe['ingredients']))
        #
        # print(f'Difficulty: {difficulty}')



#print('')
#print('Ingredients Available Across All Recipes')
#print('----------------------------------------')
#for ingredient in sorted(ingredients_list):
    #print(ingredient)

data ={'recipes_list': recipes_list, 'all_ingredients':all_ingredients}

#filename = input('Type the name of the file to store recipes: ')
with open(filename,'wb') as file_stream:
   pickle.dump(data, file_stream)
   print('saved successfully')
   
    
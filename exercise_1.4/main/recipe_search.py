import pickle

def display_recipe(recipe):
    print('name: ', recipe['name'])
    print ('cooking_time_minutes: ', recipe['cooking_time'])
    print('ingredients: ' + ', '.join(recipe['ingredients']))
    print('difficulty: ', recipe['difficulty'])

def search_ingredients(data):
    ingredients_list= data['all_ingredients']
    recipes_list = data['recipes_list']

    for index, ingredient in enumerate(ingredients_list):
        print (f'{index} \t {ingredient}')

    try:
        choose_index = int(input('enter the valid number: '))
        ingredient = ingredients_list[choose_index]
        ingredient = ingredient.lower()
    except IndexError:
        print ('the number is not valid.')
    except:
        print('unexpected error occured')
    else:
        print('recipies that contain the selected ingredient: ')
        print('')
        for recipe in recipes_list:
            if ingredient in recipe['ingredients']:
                display_recipe(recipe)

if __name__=='__main__':

    filename =input ('enter the filename where you have stored your code: ')
    try:
        with open(filename,'rb') as file_stream:
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
    else:
        search_ingredients(data)




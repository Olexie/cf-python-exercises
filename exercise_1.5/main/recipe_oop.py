class Recipe(object):

    all_ingredients =[]

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time_minutes = int(0)
        self.difficulty =''

    def get_name(self):
        output = 'Recipe name: ' + str(self.name)
        return output
    
    def set_name(self, name):
        self.name = str(name)

    def get_cooking_time_minutes(self):
        output = 'Cooking time in minutes: ' + str(self.cooking_time_minutes)
        return output
    
    def set_cooking_time_minutes(self, cooking_time_minutes):
        self.cooking_time_minutes = int(cooking_time_minutes)

    def add_ingredients(self, *args):
        self.ingredients = args
        self.update_all_ingredients()

    def get_ingredients(self):
        print('\nIngredients: ')
        print('---------------')
        for ingredients in self.ingredients:
            print(' - ' + str(ingredients))
            print('\n')

    def get_difficulty(self):
        difficulty = self.calc_difficulty(self.cooking_time_minutes, self.ingredients)
        output = 'difficulty: ' + str(self.cooking_time_minutes)
        self.difficulty = difficulty
        return output
    
    def calc_difficulty(self, cooking_time_minutes, ingredients):
        if (cooking_time_minutes < 10) and (len(ingredients)< 4):
            difficulty = 'Easy'
        elif (cooking_time_minutes < 10) and (len(ingredients) >= 4):
            difficulty = 'Medium'
        elif (cooking_time_minutes >= 10) and (len(ingredients) < 4):
            difficulty = 'Intermediate'
        elif (cooking_time_minutes >= 10) and (len(ingredients) >= 4):
            difficulty = 'Hard'
        else:
            print ('Something went wrong')

        return difficulty
    
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    def search_ingredient(self, ingredient, ingredients):
        if(ingredient in ingredients):
            return True
        else:
            return False
        
    def recipe_search (self, recipe_list, ingredient):
        data = recipe_list
        search_term = ingredient
        for recipe in data:
            if self.search_ingredient(search_term, recipe.ingredients):
                print (recipe)


    def __str__(self):
        output = '\nName: ' + str(self.name) + \
            '\nCooking time in minutes: ' + str(self.cooking_time_minutes) + \
            '\nDifficulty: ' + str(self.difficulty) +\
            '\nIngredients: ' + \
            '\n-----------\n'
        for ingredient in self.ingredients:
            output += ' - ' + ingredient +'\n'
        return output
    
    def view_recipe(self):
        print('\nName: ' + str(self.name))
        print('Cooking time: ' + str(self.cooking_time_minutes))
        self.get_ingredients()

recipes_list =[]

tea = Recipe('Tea')
tea.add_ingredients('Tea leaves', 'Water', 'Sugar')
tea.set_cooking_time_minutes(5)
tea.get_difficulty()

recipes_list.append(tea)

coffee = Recipe('Coffee')
coffee.add_ingredients('Coffe powder', 'Water', 'Sugar')
coffee.set_cooking_time_minutes(5)
coffee.get_difficulty()

recipes_list.append(coffee)

cake = Recipe('Cake')
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk')
cake.set_cooking_time_minutes(50)
cake.get_difficulty()

recipes_list.append(cake)

banana_smoothie = Recipe('Banana Smoothie')
banana_smoothie.add_ingredients ('Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes')
banana_smoothie.set_cooking_time_minutes(5)
banana_smoothie.get_difficulty()

recipes_list.append(banana_smoothie)


print ('--------')
print('Recipies List: ')
print ('-------')
for recipe in recipes_list:
    print(recipe)

print('----------')
print('Results for recipe_search with Water: ')
print('-----------')
tea.recipe_search(recipes_list, 'Water')


print ('---------')
print('Results for recipe_seaerch with Sugar: ')
print('---------')
tea.recipe_search(recipes_list, 'Sugar')

print('------')
print('Results for recipe_search with Bananas: ')
print('--------')
cake.recipe_search(recipes_list, 'Bananas')


        
                        

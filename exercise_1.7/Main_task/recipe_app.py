
#connecting database 
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://cf-python:password@localhost/my_database")

#generate the declarative base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column
from sqlalchemy.types import Integer, String

#declaring recipe class that is inherited from the Base
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time_minutes = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
    def __str__(self):
        output = "\nName: " + str(self.name) + \
           "\nCooking time minutes: " + str(self.cooking_time_minutes) + \
           "\nIngredients: " + str(self.ingredients) + \
           "\nDifficulty: " +str(self.difficulty)
        return output
    
    #create tables of models defined
Base.metadata.create_all(engine)

    #create sessionobject to make changes to the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

def calc_difficulty(cooking_time_minutes, recipe_ingredients):
        print(" Check the difficulty: ", cooking_time_minutes, recipe_ingredients)

        if(cooking_time_minutes < 10) and (len(recipe_ingredients) < 4):
            difficulty_level = "Easy"
        elif(cooking_time_minutes < 10 ) and (len(recipe_ingredients) >= 4):
            difficulty_level = "Medium"
        elif(cooking_time_minutes >= 10 ) and (len(recipe_ingredients) < 4):
            difficulty_level = "Intermediate"
        elif (cooking_time_minutes >= 10) and (len(recipe_ingredients)>= 4):
            difficulty_level = "Hard"
        else:
            print("Somethig went wrong, please try again")

        print("Difficulty level: ", difficulty_level)
        return difficulty_level
    
def return_ingredients_as_list():
        #assigning all resipes to recipe  list
        recipes_list = session.query(Recipe).all()
        for recipe in recipes_list:
            print("Recipe: ", recipe)
            print("recipe.ingredients: ", recipe.ingredients)
            recipe_ingredients_list = recipe.ingredients.split(", ")
            print(recipe_ingredients_list)


    # creating a new recipe data
def create_recipe():
        recipe_ingredients =[]

        correct_input_name = False
        while correct_input_name == False:
            name = input("\nEnter the name of the recipe: ")
            if len(name) < 50:

                correct_input_name =True

                correct_input_cooking_time_minutes = False
                while correct_input_cooking_time_minutes == False:
                    cooking_time_minutes = input("\nEnter the cooking time: ")
                    if cooking_time_minutes.isnumeric() == True:
                       correct_input_cooking_time_minutes = True

                    else:
                      print("Please enter a number")
        else:
            print("The name should contain less than 50 characters.")

        correct_input_number = False
        while correct_input_number == False:
            ing_nber = input("How many ingredients would you like to enter?: ")
            if ing_nber.isnumeric()==True:
                correct_input_number = True

                for _ in range(int(ing_nber)):
                    ingredient = input("Enter an ingredient: ")
                    recipe_ingredients.append(ingredient)
        else:
            correct_input_number = False
            print ("Please enter a positive number")

    # Converting list of ingredients into a string
recipe_ingredients_str = ", ".join(recipe_ingredients)
print(recipe_ingredients_str)

difficulty = calc_difficulty(int(cooking_time_minutes), recipe_ingredients)

recipe_entry = Recipe(
        name = name,
        cooking_time_minutes = int(cooking_time_minutes),
        ingredients = recipe_ingredients_str,
        difficulty = difficulty
    )

print(recipe_entry)

session.add(recipe_entry)
session.commit()

print("Recipe saved successfully")


    #viewing all recipes
def view_all_recipes():
        all_recipes=[]
        all_recipes = session.query(Recipe).all()

        if len(all_recipes) == 0:
           print("there is no recipe")
           return None
        else:
            print("\nFind all the recipes below: ")
            print("-"*7)
        for recipe in all_recipes:
            print(recipe)


    #search by ingredient
def search_by_ingredient():
        if session.query(Recipe).count()== 0:
            print("The recipe doesn't exist")
            return None
        else:
            results = session.query(Recipe.ingredients).all()
            print("Results: ", results)

            all_ingredients =[]

            for recipe_ingredients_list in results:
                for recipe_ingredients in recipe_ingredients_list:
                    recipe_ingredient_split = recipe_ingredients.split(", ")
                    all_ingredients.extend(recipe_ingredient_split)
            print("all_ingredients after the loop: ",all_ingredients)

            all_ingredients = list(dict.fromkeys(all_ingredients))

            all_ingredients_list = list(enumerate(all_ingredients))

            print("\nAll ingredients: ")
            print("-"*7)

            for index, tup in enumerate(all_ingredients_list):
                        print(str(tup[0]+1) + ". " + tup[1])

            try:
                        ingredient_searched_nber = input("\nEnter the number corresponding number from the list above")

                        ingredients_nber_list_searched = ingredient_searched_nber.split(" ")

                        ingredient_searched_list =[]

                        for ingredient_searched_nber in ingredients_nber_list_searched:
                            ingredient_searched_index = int(ingredient_searched_nber) - 1
                            ingredient_searched = all_ingredients_list[ingredient_searched_index][1]

                            ingredient_searched_list.append(ingredient_searched)
                        print("\nIngredients selected: ", ingredient_searched_list)


                        conditions =[]

                        for ingredients in ingredient_searched_list:
                            like_term = "%"+ingredient+"%"

                            condition = Recipe.ingredients.like(like_term)
                            conditions.append(condition)
                        print(" Conditions: ", conditions)

                        searched_recipes = session.query(Recipe).filter(*conditions).all()

                        print(searched_recipes)

            except:
                        print("Inexpecyed error occured")

            else:

                        print("searched_recipes: ")
                        for recipe in searched_recipes:
                            print(recipe)
                        
def delete_recipe():

        if session.query(Recipe).count() == 0:
          print("Recipe doesn't exist")
          return None
        
        else:
            results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
            print("results: ", results)
            print("Available recipes: ")

            for recipe in results:
                print("\nID: ", recipe[0])
                print("\nName: ", recipe[1])

            recipe_id_for_deletion = int(input("\n Enter the ID of the recipe you wish to delete: "))

            recipe_to_be_deleted = session.query(Recipe).filter(Recipe.id == recipe_id_for_deletion).one()

            print("\nAre you sure you want to delete this recipe?: ")
            print(recipe_to_be_deleted)

            deletion_confirmed = input("\nConfirm your choice (y/n): ")
            if deletion_confirmed == "y":
                session.delete(recipe_to_be_deleted)

                session.commit()
                print("\nRecipe has been deleted")
            else:
                return None
            
def edit_recipe():
    if session.query(Recipe).count()==0:
        print("This Recipe doesn't exist")
        return None
    else:
        results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
        print("results: ", results)
        print("List of the recipies: ")
        for recipe in results:
            print("\nID: ", recipe[0])
            print("\nName: ", recipe[1])

        recipe_id_for_edit = int((input("\nEnter the ID of the recipe you want to edit: ")))


        print(session.query(recipe).with_entities(Recipe.id).all())
        recipes_id_list = []

        for recipe_tup in recipes_id_tup_list:
            print("recipe_tup[0]")
            recipes_id_list.append(recipe_tup[0])
        
        print(recipes_id_list)

        if recipe_id_for_edit not in recipes_id_list:
            print("Not in the ID list")
        else:
            print("continue")

            recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).one()

            print("\nYou about to edit this recipe: ")
            print(recipe_to_edit)


            column_for_update = int(input("\nEnter the data you want to update"))

            update_value = (input("\nEnter the new value: "))
            print("Choice: ", update_value)


            if column_for_update ==1:
                print("You've selected the name to update")
                session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.name: update_value})
                session.commit()

            elif column_for_update == 2:
                print("you've selected the cooking time for update")
                session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.cooking_time_minutes: update_value})
                session.commit()

            elif column_for_update == 3:
                print("You've selected ingredients to update")
                session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.ingredients: update_value})

            else:
                print("wrong input")
            
            update_difficulty = calc_difficulty(recipe_to_edit.cooking_time_minutes, recipe_to_edit.ingredients)
            print("update_difficulty", update_difficulty)

            recipe_to_edit_difficulty = update_difficulty

            session.commit()
            print("changes done")

def main_menu():
    choice=""
    while(choice != "stop"):
        print("\n===========================")
        print("\nMain Menu: ")
        print("----------------------------")
        print("\nMake a choice: ")
        print("   1. Create a new recipe")
        print("   2. Search for a recipe by ingredient")
        print("   3. Edit an existing recipe")
        print("   4. Delete a recipe")
        print("   5. View all recipes")
        print(" \nType 'stop' to exit" )
        choice = input("\nYou've chosen: ")
        print("\n=====================================")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            search_by_ingredient()
        elif choice == "3":
            edit_recipe(recipe_ingredients)
        elif choice == "4":
            delete_recipe()
        elif choice == "5":
            view_all_recipes()
        else:
            if choice == "stop":
             print("Thank you!\n")
            else:
                print("Try again")


main_menu()
session.close()
        



       


            
    

          


                


                


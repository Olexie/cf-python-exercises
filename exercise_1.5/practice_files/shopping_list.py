class ShoppingList(object):
    def __init__(self, list_name):
        shopping_list =[]
        self.list_name = list_name
        self.shopping_list = shopping_list

        #add item to a shopping list
    def add_item(self, item):
         self.iem = item

         if(item in self.shopping_list):
             print('The item has already been added')
         else:
            self.shopping_list.append(item)
            print('New item is added')

         #remove item from the shopping list
    def remove_item(self, item):
          self.item = item
          if (item in self.shopping_list):
              self.shopping_list.remove(self.item)
              print('item has been removed from the list')
          else:
              print('the item is not in the list')

     
    def view_list(self):
        print(self.shopping_list)
        print('shopping list content ' + self.list_name + ': ')
        print('--------')
        for item in self.shopping_list:
            print('- ' + item)
        

#intitializing list

pet_store_list = ShoppingList('Pet store shopping list')
pet_store_list.add_item('cat food')
pet_store_list.add_item('bowl')
pet_store_list.add_item('treats')
pet_store_list.add_item('flea collar')
pet_store_list.add_item('cat toy')

pet_store_list.remove_item('flea collar')

pet_store_list.add_item('mouse')

pet_store_list.view_list()
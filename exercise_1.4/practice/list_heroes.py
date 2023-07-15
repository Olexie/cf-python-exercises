def display (file):
    heroes =[]
    for line in file:
        line = line.rstrip('\n')
        hero_name = line.split(', ') [0]
        first_appearence = line.split(', ') [1]

        heroes.append([hero_name, first_appearence])

    heroes.sort (key=lambda hero: hero[1])  

    for hero in heroes:
            print('-------------------')  
            print('Superhero: ' + hero[0])
            print ('First year of aapearence: ' + hero[1])  

filename = input ('Enter the filename where you have stored your superheroes: ')   
try:
     file = open(filename, 'r')
     display(file)
except FileNotFoundError:
     print('File does not exist - exiting.')
except:
     print('An unexpected error occured.')
else:
     file.close()
finally:
     print('Goodbye')   
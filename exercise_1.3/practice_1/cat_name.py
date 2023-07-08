cat_name =input('name your cat: ')
if cat_name == 'kokos':
    print('ginger')

    cat_age = input('how old is your cat: ')
    if int(cat_age) >= 8:
        print('oldster')
    else:
        print('youngster')

elif cat_name == 'miso':
    print('grey')
else: 
    print('unknown colour')
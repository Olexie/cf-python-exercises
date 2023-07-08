def capitalisation_plus_A(variable1='orange'):

    output = variable1 + 'A'
    return output


cat_names =['miso', 'mochi', 'marsik', 'kokos']
for name in cat_names:
    my_result = capitalisation_plus_A(name)
    print(my_result)


a = int(input("Enter a number: "))
b = int(input("Enter another number to be added to the first: "))

if a > b:
    print('a is bigger than b')
elif b>a:
    print('b is bigger than a')
elif a==b:
    print('a is equal to b')
else:
    print('no matches')



print("The sum of these numbers is " + str(a + b))
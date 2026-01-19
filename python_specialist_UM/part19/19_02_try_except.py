#this is about some developed try/except Methode inside of our code
#as we can learn further we have 3 kind of Error .
# now we try to set 3 diffrent except for our first code:
# ok againtest it
items = ['a', 'b']

try:
    #we set 3 diffrent mistake in our code:
    #myvar= a
    x = 10/0
    third = items[2]
    
except ZeroDivisionError:
    print("You can not divid by Zero!")

except IndexError:
    print("Index out of bounds")

except NameError:
    print("Tried to fetch a name that did not Exist!")



print("this does RUN!")

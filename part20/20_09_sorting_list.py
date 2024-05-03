'''
#example 1: 
#so now we test anotother type to sorting a list:
#1. first of all we have a list for some Fruits like this
L = ["Cherry", "Apple", "Blueberry"]

#now we try to sort the list with key as len >> how long will be one word
print(sorted(L, key=len))
#alternative form using lambda, if you find that easier to understand
print(sorted(L, key= lambda x: len(x)))
'''

#example 2 :
# we have now another example for sorting the list with using the price of them:

class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)
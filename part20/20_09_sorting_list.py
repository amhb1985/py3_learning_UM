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

#1. we have one class as Fruit():
class Fruit():
    #2. then we define now with __init__ (self, name>> forFruits,  price >> for Fruit):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    #2.2 now we can define another init for sorting the result
    def sort_priority(self):
        return self.price

    #3. we set one List L=[] and then we add Fruits in it:
L = [Fruit("Cherry", 10),
     Fruit("Apple", 5),
     Fruit("Blueberry", 20)
]
    #4. we sort it:
#for f in sorted(L, key=lambda x: x.price):
    #print(f.name)
    #print(f.price)
vegatable = ("Tomato" , 15)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)
    print(f.price)

#so now we test anotother type to sorting a list:
#1. first of all we have a list for some Fruits like this
L = ["Cherry", "Apple", "Blueberry"]

#now we try to sort the list with key as len >> how long will be one word
print(sorted(L, key=len))
#alternative form using lambda, if you find that easier to understand
print(sorted(L, key= lambda x: len(x)))

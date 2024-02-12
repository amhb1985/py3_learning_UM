#11.4.1. Iterating over Dictionaries
'''
inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys(): 
     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())       # Make a list of all of the keys
print(ks)
print(ks[0])                      # Display the first key


'''
inventory02 = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory02:
    print("Got key", k)

    

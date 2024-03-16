
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]

#first of all we can see the one element from the 
print(nested1[0])

#2. we can count the list with len()
print(len(nested1))
#3. we append and add another element in list with .append(['i'])
nested1.append(['i'])

print("-------")
#we can see the all of the List:
print(nested1)
print("-------")

for L in nested1:
    print(L)

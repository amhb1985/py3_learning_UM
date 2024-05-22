
#ListMethode
# review again

mylist = []
mylist.append(5)
mylist.append(5)
mylist.append(27)

#mylist.append(3)
#mylist.append(12)


mylist.insert(1, 12)
print(mylist)
#Add another 5 in the List for counting: ".count((5))"
print(mylist.count(5))

#print(mylist.index(3))
print(mylist.count(5))

print("revrese_List:")
mylist.reverse()

print("sort:")
mylist.sort()
print(mylist)

print("remove 5 from List:")
mylist.remove(5)
print(mylist)

print("Last Item is:")
lastitem = mylist.pop()
print(lastitem)
print(mylist)

#test nochmal

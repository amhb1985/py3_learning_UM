#Mutability
# we can set an new data to list :
'''fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "Kiwi"
print(fruit)


#remove or delet from list:
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

'''

#another form to delet :
a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)



#insert or add one data to list (with the number)
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)

alist[4:4] = ['e']
print(alist)
'''

#string change :
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was

print(type(greeting))
print(type(newGreeting))
'''

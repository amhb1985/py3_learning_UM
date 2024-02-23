

#chnaging the list of student to City name
'''
def changeit(lst):
    lst[0] = "Berlin"
    lst[1] = "atlanta"


mylst = ['our', 'students', 'are', 'awesome']

#we can change one list as func with command : changeit(). 
changeit(mylst)
print(mylst)


def myfun(lst):
    lst = [1, 2, 3]

mylist = ['a', 'b']

#chnage all of list
myfun(mylist)
print(mylist)
'''

#change the list with commend del list  :
def myfun(lst):
    #we can set am exact delet to function:
    del lst[1]

mylist = ['a', 'b', 'c','d']

myfun(mylist)

#here we can see the change just the exact Index 
print(mylist)
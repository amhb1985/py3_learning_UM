
#this is abour user defined Classes

# we set the class for our X , Y :
# Not: we must after set Class return it with pass!
class Point():
    pass
point1 = Point()
point2 = Point()

# after running the print we can see that we have two diffrent Object in our Class
#print(point1)
#print(point2)

# now we can check the result of class
# we can see that point1 is NOT equal pont2 !
'''
print(point1 == point2)
print(point1 != point2)
'''
#so we can set a formula for our points: with " .x = "

point1.x = 5 
point2.x = 10 
print(point1.x)
print(point2.x)






#this is abour user defined Classes

# we set the class for our X , Y :
# Not: we must after set Class return it with pass!


#so now we change the all of ckasses with define 
#Not:Methods belongs Classes
class Point():
    def getX(self):
        return self.x
    
point1 = Point()
point2 = Point()

# after running the print we can see that we have two diffrent Object in our Class
#print(point1)
#print(point2)

# now we can check the result of class
# we can see that point1 is NOT equal pont2 !
#test and review🧐
print(point1 == point2)
print(point1 != point2)

#so we can set a formula for our points: with " .x = "
#then we can change the point.x to our define as get.x and run the all of code and we'll see the same result as 5 
point1.x = 5 
point2.x = 10 
print(point1.getX())
print(point2.getX())








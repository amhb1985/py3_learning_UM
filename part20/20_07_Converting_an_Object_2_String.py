# so this is about converting an Object to the String in one Class :
# for the first Example we can test below: 
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    #for the solve of it we must >> define a def __str__ (self) and exactly return it
    def __str__(self):
        #then we can see the 'Point'
        return('Point 123')


#so after the running the test we will see that just one message :<__main__.Point object at 0x7f5549b8bfd0> 
p = Point(7,6)
print(p)

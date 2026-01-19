#this lection about the intace as value in class

#0. we another ones we must create one class in our script:

class Point:

    #1. in the our class first we r defining the init (self, init for X AND Y)
    def __init__(self, initX, initY):
        #1.1 we set the delf file with our init()
        self.x = initX
        self.y = initY
    
    #2. now we are defining the getX(self) and getY(self) NATURALLY with the return commend:
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    #3. then we can set our formular or in another hand define it, Like these:
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    #4. we must notice that we must define string(self)
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)
    #5. we can define another formula for hafway:
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
#6. we can set now two list varibles for our X,Y as p, q or z
p = Point(3,4)
q = Point(5,12)
#7. we can set another formula for our p and q
mid = p.halfway(q)
# note that you would have exactly the same result if you instead wrote
# mid = q.halfway(p)
# because they are both Point objects, and the middle is the same no matter what


print(mid)
print(mid.getX())
print(mid.getY())


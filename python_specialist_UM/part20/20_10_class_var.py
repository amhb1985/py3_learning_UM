# this chapter is about the class varible and Instace varible:

#0: we set a class for our points:
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    # we can set * for our rep  or we can change it to x or <<
    printed_rep = " << "

    #1. we define two Functions for our ponits:
    #1.1 we define the first init for our points as x and y
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    #2.  we define another Function for as graf and 
    # inside of graf we set sone another commend:
    def graph(self):
        # 2.1 so first we need 2 lists >>one empty list for rows >>two for size
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        # 2.2 then we create a LOOP for the range with the 2nd list >> size
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)

# so we test now 2 points lists:
# and then we'll chang it:
p1 = Point(2, 30)
p2 = Point(3, 12)
print(p1.graph())
print(p2.graph())

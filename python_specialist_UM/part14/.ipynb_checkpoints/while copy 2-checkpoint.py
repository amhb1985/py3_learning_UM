

#the while (Loop )statment:


def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """

    theSum  = 0 #the sum so far
    aNumber = 1 #where we are 1> 2> 3> 4 ...aBand

    #whle ..... >>> return ..
    while aNumber <= aBound:  #is less than or equal
        theSum = theSum + aNumber #0 +1 = 1
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))

print(sumTo(1000))
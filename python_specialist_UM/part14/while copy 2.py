

#the while (Loop )statment:
#definition a Sum 
def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """
    theSum  = 0 #the sum so far
    #we test again for anither test with 2
    aNumber = 2 #where we are 1> 2> 3> 4 ...aBand

    #whle ..... >>> return ..
    while aNumber <= aBound:  #is less than or equal
        theSum = theSum + aNumber #0 +1 = 1
        #changing to a Number+2
        aNumber = aNumber + 2
    return theSum

print(sumTo(4))

print(sumTo(1000))
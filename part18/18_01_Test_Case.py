# as the first code we use this code:

#for example define a Function for squre of X:
def square(x):
    return x + x

#so after searching in Internet id release that we must correct the import test as from test import testEqual
#01 first we must import it
from test import testEqual 

#then we print our result:
print('testing squre function')
#03. we must testning  testEquel >> ourFunction (the X), and the Answere
#>> when the answere will true , then comming TRUE as 'Pass'!! in another hand comming the 'TEST Failed'
#>> so for the first Try unfortionatly we can not un it, may bee we must change the testEqual to new Version


test.testEqual(square(10),100)
#testing with anothers:
test.testEqual(square(3),9)
test.testEqual(square(-4),16)
test.testEqual(square(1.5),2.25)
test.testEqual(square(0),0)
test.testEqual(square(2),4)

#so we cann not see the result bcos of test Equal
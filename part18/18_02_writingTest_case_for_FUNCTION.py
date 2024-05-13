
#unfortunatly its just for the Py IDE in fopp: 
import test

#test sorted()
test.testEqual(sorted([1, 7, 4]), [1, 4, 7])

#test reverse
test.testEqual(sorted([1, 7, 4], reverse=True), [7, 4, 1])

#test reverse with false
test.testEqual(sorted([1, 7, 4], reverse=False), [1, 4, 7])
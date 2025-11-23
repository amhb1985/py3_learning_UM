'''
#unfortunatly its just for the Py IDE in fopp: 
import test

#test sorted()
test.testEqual(sorted([1, 7, 4]), [1, 4, 7])

#test reverse
test.testEqual(sorted([1, 7, 4], reverse=True), [7, 4, 1])

#test reverse with false
test.testEqual(sorted([1, 7, 4], reverse=False), [1, 4, 7])
'''

#testing again with the side Effect
# so now we test the side Effects 

#1. first of all we must define a Function as update_counts_d:
def update_counts(letters, counts_d):
    #1.1 set one Loop inside of Function for the first item as letters
    for c in letters:
        counts_d[c] = 1
        #1.2  set if for c for the secound parmeter(item) of Function:
        if c in counts_d: 
            counts_d[c] = counts_d[c] + 1

#then we must import test but we dont have allow to import test
import test 

# try to test with one example: here with one Dictionary like counts.
counts = {'a':3, 'b':2}
update_counts("aaab", counts)

test.testEqual(counts['a'], 6)
test.testEqual(counts['b'], 3)

counts = {'a':3, 'b':2}
update_counts("", counts)
test.testEqual(counts['b'], 3)








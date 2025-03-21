#Write a function called subtract_three that takes an integer 
#or any number as input, and returns that number minus three.

#its easy we can just set first an function with def and the name with Number
# and then we must use the -3 for return
'''
def subtract_three(number):
    return number - 3
'''
## A accumulates / Funcion 
#so 1. we creare a func and then..
#2. we name seq
def mylen(seq):
    c = 0 # initialize count variable to 0
    for _ in seq:
        c = c + 1   # increment the counter for each item in seq
    return c

#so we can know calculate all of the words or Numbers withe set in mylen()!
print(mylen("hello"))
print(mylen([1, 7]))


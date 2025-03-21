#this is about the FUNCTION ZIP IN Py3:

#1. for the undersatnding the function of Zip in the py3 we can explain 
# a similary append as i learnd before:
'''
# we can see that we have 2 diffrent Lists and we can append both of them in list3:
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)


'''
'''
#2. so now we can use the zip function in Py3:

#1 we have 2 diffrent list:
L5 = [3, 4, 5]
L6 = [1, 2, 3]
#we can zip both of them with list(zip())
L10 = list(zip(L5, L6))
# in adition we can set a Dict instead of list:
L11 = dict(zip(L5, L6))
print(L11)
print(L10)
'''
#3. we can sset the zip like the first example
'''
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))
L5 = dict(zip(L1, L2))
print("the pure result of 'ZIP' as  " ,type(L4), "is:   ",L4)
print("the pure result of 'ZIP' as  " ,type(L5), "is:   ",L5)

#Not: we must use Loop from 
for (x1, x2) in L4:
    L3.append(x1+x2)

print("the result of 'ZIP' with Loop & append   " ,type(L4), "is :",L3)
'''
# so  naother example for the game hangmann with Anrea is like it:
# we will set another def()
def compatible_char(bc, wc, guess_made):
    if bc == '_' and wc in guess_made:
        return False
    elif bc != '_' and bc != wc :
        return False 
    else:
        return True

# 1. we define one defintion as possible with 3 element as (word >>> blaned >>> guessmade)
def possible(word, blanked, guesses_made):
    #2 set the first the number of guess word with the number of blanked if >> is not !=
    if len(word) != len(blanked):
        return False
#now we can set a zip function:
    for (bc, wc) in zip(blanked, word):
        if not compatible_char(bc , wc, guesses_made):
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))








    
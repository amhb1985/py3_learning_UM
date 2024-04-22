#this is about the FUNCTION ZIP IN Py3:

#1. for the undersatnding the function of Zip in the py3 we can explain 
# a similary append as i learnd before:

# we can see that we have 2 diffrent Lists and we can append both of them in list3:
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)



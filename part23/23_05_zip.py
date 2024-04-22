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
#2. so now we can use the zip function in Py3:

#1 we have 2 diffrent list:
L5 = [3, 4, 5]
L6 = [1, 2, 3]
#we can zip both of them with list(zip())
L10 = list(zip(L5, L6))
print(L10)


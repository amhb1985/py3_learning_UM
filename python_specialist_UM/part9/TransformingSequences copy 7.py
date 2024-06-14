#Accumulator Pattern with Lists¶


#1. set an list as Numbers:
nums = [3, 2, 8]

#2. set the newlist for Accuulation
accum = []

#3. set Loop for each Element 
for w in nums:

    #3.01 in every element in list "nums" macke an math as name "x":
    x = w**2

    #03.02 append or add this loop as "x" to the list:
    accum.append(x)

print(accum)
print(nums)
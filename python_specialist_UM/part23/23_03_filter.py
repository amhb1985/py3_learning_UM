#this is about filter
'''
#1. creat one def
def keep_evens(nums):
    #2. creat a new empty List
    new_list = []

    #3. set one Loop with for Number in Numbers:
    for num in nums:
        #3_1 : set  filter with IF 
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

'''
'''
#set 2nd example:

def keep_evens(nums):
    #set with lambda with filter: 
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))

'''

#2. Using filter, filter lst so that it only contains words containing the letter “o”.
# Assign to variable lst2. Do not hardcode this.
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
# new varible and set this as main:
#lst2 = filter(<some filtration function>, lst)

lst2 = filter(lambda word: "o" in word, lst)



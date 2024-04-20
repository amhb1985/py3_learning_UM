#this is about filter

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

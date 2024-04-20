'''
#we have here one List
things = [2, 5, 9]

#we creat one value as Transformer expression  FORMULA list but here for value in things
yourlist = [value * 2 for value in things]

yourlist = map (lambda value: value*2, things)
print(yourlist)

'''

def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))
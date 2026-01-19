'''
#we have here one List
things = [2, 5, 9]

#we creat one value as Transformer expression  FORMULA list but here for value in things
yourlist = [value * 2 for value in things]

yourlist = map (lambda value: value*2, things)
print(yourlist)

'''
'''
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

'''
#tset
#3_ example You can also combine map and filter operations by chaining them together, or with a single list comprehension.
things = [3, 4, 6, 7, 0, 1, 4]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])


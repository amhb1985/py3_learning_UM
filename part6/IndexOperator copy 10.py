'''
this is the py test for the index
and about some training in Py3 
'''

# so we are trying to join these variable:


by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = by + az + io + qy
#print (message)

#for the count .count()
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
how_many= nums.count(2)
#print (how_many)


nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

# Find the index of the second occurrence of 8
index_of_second_8 = nums.index(8, nums.index(8) + 1)

# Use slicing to remove the second occurrence of 8
nums = nums[:index_of_second_8] + nums[index_of_second_8 + 1:]

#print(nums)

#Assign the number of elements in lst to the variable num_lst.
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]
num_lst = len(lst)

#print(num_lst)
weather = ["sunny", "cloudy", "partially sunny", "rainy", "storming", "windy", "foggy", "snowy", "hailing"]

for condition in weather:
    first_char = condition[0]
    last_char = condition[-1]

    print("The first character is: " + first_char)
    print("The last character is: " + last_char)
    print("The word is", len(condition), "characters")
    print()  # Add a newline for better readability between items

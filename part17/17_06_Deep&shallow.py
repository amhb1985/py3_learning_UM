'''
#first we must have a List as Dictionary:
original = [['dogs', 'puppies'], ['cats', "kittens"]]
#we creat one list as copy with [:]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)

original[0].append(["canines"])
print(original)

print("--------Now look at the copied version -----------")
print("-------- Now look at the copied version -----------")

print(copied_version)

'''
'''
#2: 
# our orginal list is:
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)
'''


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
#import majol of copy
import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])

#because of . append in our Org list we'll see the str: "Hi there"
print("-------- our Original List :-----------")
print(original)

print("-------- deep copy  -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)

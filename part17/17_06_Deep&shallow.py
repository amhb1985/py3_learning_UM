
original = [['dogs', 'puppies'], ['cats', "kittens"]]
#we creat one list as copy with [:]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)
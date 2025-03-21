

#What will the following code output?

'''def cyu2(s1, s2):
    x = len(s1)
    y = len(s2)
    return x-y

z = cyu2("Yes", "nooo")
if z > 0:
    print("First one was longer")
else:
    print("Second one was at least as long")
    '''


def show_me_numbers(list_of_ints):
    print(10)
    print("Next we'll accumulate the sum")
    accum = 0
    for num in list_of_ints:
        accum = accum + num
    return accum
    print("All done with accumulation!")

show_me_numbers([4,2,3])
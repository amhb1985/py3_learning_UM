

nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h'],['A','B','C'],['a']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("             level2: {}".format(y))
    else:
        print(x)

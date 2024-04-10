 
#1.we need one list
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]

#2.we set an loop for x in 
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

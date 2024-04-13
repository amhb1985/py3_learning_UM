 
'''
#1.we need one list
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]

#2.we set an loop for x in our list (here is nested1) 
for x in nested1:
    print("level1: ")
    #3. again we set another loop inside of x
    for y in x:
        print("     level2: " + y)

'''
#another example:
#Below, we have provided a list of lists that contain information about people. 
#Write code to create a new list that contains every person’s last name, and save that list as last_names.


info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
'''
#the whole of the cod is a simple like this:
accum = []
for somthing in somthing:
    <refer to accum>
 '''
#1.emptylist as lastname
last_names = []

#2. set a loop
for entertainer in info:
    #3.01 : set and define witch element (here last name is entertainer[1] )
    #3.02 : then we must .append() it in to list
    last_names.append(entertainer[1])
    #print(last_names)
#print(info[1][1])
for entertainer in info:
    for val in entertainer: 
       print(val)
    pass

for val in info[1]:
    print (val)








    



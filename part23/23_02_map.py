
#this is about Map in py 3


#1. we set an definition for our Doublestuff
def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    #2.then we set an empty List:
    new_list = []
    #3. we need now one Loop for value in List
    for value in a_list:
        #3.1 set a Formula for a value
        new_elem = 2 * value
        #3.2 Append (add) the results in our value
        new_list.append(new_elem)
        #4. at end,,,, return it
    return new_list


#so we can test it for one excample with Intege 
things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)



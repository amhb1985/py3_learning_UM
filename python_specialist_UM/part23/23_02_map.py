
#this is about Map in py 3

'''
#1. we set an definition Function for our Doublestuff
def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    #2.then we set an empty List:
    new_list = []
    #3. we need now one Loop for value in List
    for value in a_list:
        #3.1 set a Formula for a value
        new_elem = (2 * value)+1
        #3.2 Append (add) the results in our value
        new_list.append(new_elem)
        #4. at end,,,, return it
    return new_list


#so we can test it for one excample with Intege 
things = [4, 3, 9]
print(things)
things = doubleStuff(things)
print(things)


'''

#2. then we ccan try the next test for the map with Triple:
#the main thing for our Def X(value):  >>> return 3 * (value) 
def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)


things = [7, 5, 10]
things3 = tripleStuff(things)
print(things3)
#things4 = quadrupleStuff(things)
#print(things4)

'''
#test
#3. another example for map is:

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def f(st):
    return st.upper()

#abbrevs_upper = map(f, abbrevs)
#another hand we can write another way like this:
abbrevs_upper = map(f, abbrevs)
abbrevs_upper = map(lambda st: st[:2].upper,abbrevs)
print(abbrevs_upper)
'''
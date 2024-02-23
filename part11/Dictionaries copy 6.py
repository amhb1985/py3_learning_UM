


#my_dict = {}  # Create an empty dictionary

# Add a key-value pair
# NOTICE : we must have just ONE KEY > ONE VALUE
#my_dict["key"] = "value"

# Example
'''
my_dict["John"] = 30

my_dict["joe"] = 20

#print all of the Dic
print(my_dict)

#print the one of exact Key:
print(my_dict["joe"])


#Memorial for the last Part as List!:
#in the List we had the .append()#

my_list = []  # Create an empty list

# Append elements to the list

my_list.append("element1")
my_list.append("element2")
my_list.append("Book")
my_list.append("Pen")



#print(my_list)


#for another methode of Dictionary we can use the Methde of the .get() 


#here we set a text data to the read as txt data , here we can use our olympics.txt :
f = open('olympics.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters

letter_counts = {} # start with an empty dictionary
letter_counts['t'] = 0  # intiialize the t counter
letter_counts['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        letter_counts[c] = letter_counts[c] + 1   # increment the t counter
    elif c == 's':
        letter_counts[c] = letter_counts[c] + 1   # increment the s counter

print("t: " + str(letter_counts['t']) + " occurrences")
print("s: " + str(letter_counts['s']) + " occurrences")

''' 

#  I wanna now try it for another Alphabet like a and b:

#0. we must open and read one txt data, here 
d = open("olympics.txt","r")
text = d.read()

#1. create an empty Dictionary as letter_counter:
letter_counter = {}  #set an empty Dictionary
letter_counter ['a'] = 0 #intiialize the a counter
letter_counter ['b'] = 0 #intiialize the b counter
for e in text:
    if e == 'a':
        letter_counter[e] = letter_counter[e] + 1  # increment the a counter
    elif e == 'b':
        letter_counter[e] = letter_counter[e] + 1 # increment the a counter


print("a: " + str(letter_counter['a']) + " occurrences")
print("b: " + str(letter_counter['b']) + " occurrences")


     


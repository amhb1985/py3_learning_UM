
'''
#Q1. The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
#set an output nested[1][2]
output = nested[1][2]
print(output)
'''
#Q2:below, a list of lists is provided. Use in and not in tests to create variables
# with Boolean values. See comments for further instructions.

'''
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
#set a yellow stringfor searching in list [BUT WICH ONE??]
yellow = 'yellow' in lst[2]

#Test to see if 4 is in the second list of lst. Save to variable ``four``
#set a 4 Int searching in list [BUT WICH ONE??]
four = 4 in lst[1]
print(four)


#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
#set a orange as string for searching in list [BUT WICH ONE??]
orange = 'orange' in lst [0]
print(orange)
'''

'''
#Q3 : Below, we’ve provided a list of lists. Use in statements to create variables 
#with Boolean values - see the ActiveCode window for further directions.
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
#set an variable as test1 searchs info(here 'hola' as string)
test1 = 'hoal' in L
print(test1)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
#set an variable as test2 and searchs info(here as List)
test2 = [5, 8, 7] in L
print(test2)
# Test if 6.6 is in the third element of list L. Save to variable name test3
#set an variable as test3 and searchs info(here as Float)
test3 = 6.6 in L[2]
print(test3)
'''
'''
#Q5:Provided is a nested 
#data structure. Follow the instructions in the comments below. Do not hard code.

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data='data' in nested

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour=24 in nested['data'] or 24 in nested['window']
print(twentyfour)    

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
li=nested['window']
whole= 'whole' not in li
print(whole)

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics= 'physics' in nested
print(physics)

'''

#Q6:The variable nested_d contains a nested dictionary with the gold medal
 #counts for the top four countries in the past three Olympics. 
 #Assign the value of Great Britain’s gold medal count from the 
 #London Olympics to the variable london_gold. 
#Use indexing. Do not hardcode.

'''
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold=nested_d['London']['Great Britain']
print(london_gold)

'''

'''
#Q7:
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
#like the 2 Question we must set the search but here is :
# >>. DICTIONARY [][] >>
#1.first must the name of DIC 
#2. must set the index [] and then [WICH LIST]
v1 =sports['swimming'][2]
print(v1)
# Assign the string 'platform' to the name v2
v2 =sports['diving'][1]
print(v2)
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 =sports['gymnastics']['women']
print(v3)
# Assign the string 'rings' to the name v4
v4 =sports['gymnastics']['men'][3]
print(v4)
'''
'''
#8: Given the dictionary, nested_d, save the medal count 
#for the USA from all three Olympics in the dictionary to 
#the list US_count.
#for thr secound test we change the US to the Germay!
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
#set an empty List as US_count
US_count = []
#2. set a Loop with for Key in our nested list
for key in nested_d:
    #2.1 set if for the searching exact key in our Dictionary as [key]:
    if 'USA' in nested_d[key]:
        #2.2 append (add) the result of our searching key info in our empty List
        US_count.append(nested_d[key]['USA'])
#at end we use the print to show our results in our List
print('USA result is : ', (US_count))

Germany = []
#2. set a Loop with for Key in our nested list
for key in nested_d:
    #2.1 set if for the searching exact key in our Dictionary as [key]:
    if 'Germany' in nested_d[key]:
        #2.2 append (add) the result of our searching key info in our empty List
        Germany.append(nested_d[key]['Germany'])
#at end we use the print to show our results in our List
print('Germany results is: ' ,(Germany))

'''
'''
#Q9:Iterate through the contents of l_of_l and assign the third element of sublist to 
#a new list called third.
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
# 1.create an empty List
third = []
# 2.create a Loop for example list list in our Source list
for list in l_of_l:
    #2.1 append (add) list[WICH ONE?] to the our epmty list
    third.append(list[2])
print(third)

'''

#Q10:
#Given below is a list of lists of athletes. Create a list, t, 
#that saves only the athlete’s name if it contains the letter “t”. 
#If it does not contain the letter “t”, save the athlete name into list other.


athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
#1. now we create two empty Lists:
t = []
other =[]
d = []
#2.we must use the loop but we need if and else
#. for our Lists in our orginal list
for lists in athletes:
    #2 >< for orginal List in :
    for athletes in lists:
        #3.1 we must set now if:
        if 't' in athletes: #searching the exact word (here as 't')
            t.append(athletes)
        elif 'd' in athletes:
            #tetst another word with elif
            d.append(athletes)
        else:
            other.append(athletes)
  
print('the words with the "t" is/are :', t)
print('___________________________')
print('the words with the "d" is/are :', d)
print('___________________________')
print('the  another words without the  "t" is/are :',other)




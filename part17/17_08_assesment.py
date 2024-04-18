
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

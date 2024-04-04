# 8.3. Logical operators:
'''
There are three logical operators: and, or, and not. All three operators take boolean operands and produce boolean values. The semantics (meaning) of these operators is similar to their meaning in English:

x and y is True if both x and y are True. Otherwise, and produces False.
x or y yields True if either x or y is True. Only if both operands are False does or yield False.
not x yields False if x is True, and vice versa.
'''
'''
x = True
y = False
print(x or y)
print(x and y)
print(not x)
'''
'''
x = 5
#print(x > 0 and x < 10)

print(x > 3)
#n = 25
#print(n % 2 == 0 or n % 3 == 0)

'''

#one test for Smart evalution for example in the airport

total_weight = int(input('Enter total weight of luggage in Kg:'))
num_pieces = int(input('Number of pieces of luggage?'))

if num_pieces != 0 and total_weight / num_pieces > 30:
   print('Average weight is greater than 30 Kilogram -> 100 € surcharge.')
if num_pieces != 0 and total_weight / num_pieces <  30:
   print ("averageWeight is OK and less than 30kg!")
print('Luggage check complete.')

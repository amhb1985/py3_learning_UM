# 8.3. Logical operators:
'''
There are three logical operators: and, or, and not. All three operators take boolean operands and produce boolean values. The semantics (meaning) of these operators is similar to their meaning in English:

x and y is True if both x and y are True. Otherwise, and produces False.
x or y yields True if either x or y is True. Only if both operands are False does or yield False.
not x yields False if x is True, and vice versa.

'''
x = True
y = False
print(x or y)
print(x and y)
print(not x)
#Non-mutating Methods on Strings
'''
upper
none
Returns a string in all uppercase
lower
none
Returns a string in all lowercase
count
item
Returns the number of occurrences of item
index
item
Returns the leftmost index where the substring item is found and causes a runtime error if item is not found
strip
none
Returns a string with the leading and trailing whitespace removed
replace
old, new
Replaces all occurrences of old substring with new
format
substitutions
Involved! See String Format Method, below
'''

ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

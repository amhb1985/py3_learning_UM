#11.06 Accumulating  multiple results in a Dictionsry:

#If we want to find out how often the letter ‘t’ occurs, we can accumulate the result in a count variable.

f = open('squared_numbers.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the counter
print("t: " + str(t_count) + " occurrences")


#11.06  We can accumulate counts for more than one character as we traverse the text. 
#Suppose, for example, we wanted to compare the counts of ‘t’ and ‘s’ in the text.
f = open('squared_numbers.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
s_count = 0 # initialize the s counter accumulator as well
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the t counter
    elif c == 's':
        s_count = s_count + 1
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")



#11.06 Accumulating  multiple results in a Dictionsry:

#If we want to find out how often the letter ‘t’ occurs, we can accumulate the result in a count variable.

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the counter
print("t: " + str(t_count) + " occurrences")


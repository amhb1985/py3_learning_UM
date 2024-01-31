#count the charachter but First not len()!!
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."

numbs = 0

for char in str1:
    numbs += 1

print("Number of characters in str1:", numbs)

#and with len you can see:
numb = len(str1)
print("Counter with len :", numb )



numbers = list(range(41))
sum1 = 0
for w in numbers:
    sum1 = sum1 + 1
print(sum1)

sum1 = sum(numbers)

# Print the result at end:
print("Sum of the numbers from 0 through 40:", sum1)

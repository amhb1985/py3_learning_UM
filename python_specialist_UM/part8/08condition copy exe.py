'''
variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.

Hard-coded answers will receive no credit.

Original - 1 of 1

1
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
2
​'''
'''
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Split the sentence into words
words = sentence.split()

# Initialize a counter for words that start and end with the same letter
same_letter_count = 0

# Iterate through the words
for word in words:
    # Check if the word is not empty and its first and last characters are the same (ignoring case)
    if word and word[0].lower() == word[-1].lower():
        same_letter_count += 1

print("Number of words starting and ending with the same letter:", same_letter_count)
'''



'''
Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.

HINT 1: Use the accumulation pattern!

HINT 2: the in operator checks whether a substring is present in a string.

Hard-coded answers will receive no credit.
'''

'''
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

​items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama", "tumultuous", "owing"]

# Initialize a variable to store the count
acc_num = 0

# Iterate through the items in the list
for item in items:
    # Check if the character 'w' is present in the current item
    if 'w' in item:
        # If 'w' is present, increment the count
        acc_num += 1

# Print the final count
print("Number of strings containing 'w':", acc_num)
'''


#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.



s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"

vowels = ['a','e','i','o','u']

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a', 'e', 'i', 'o', 'u']

# Initialize a variable to store the count of vowels
num_vowels = 0

# Iterate through each character in the string
for char in s:
    # Check if the character is a vowel
    if char in vowels:
        # If it's a vowel, increment the count
        num_vowels += 1

# Print the total count of vowels
print("Number of vowels:", num_vowels)


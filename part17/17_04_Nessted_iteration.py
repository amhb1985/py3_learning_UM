

'''
#thge questeion is :
Below, we have provided a list of lists named L. Use nested iteration to save every string 
containing “b” into a new list named b_strings.
'''
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
#1. we must creat one empty list
b_strings = []
#2. we create LOOP for list in  and  for word in lst:
                #2.1 if somthing_sbout_word  in word:
                #2.2 (ouremptylist>> #1).append(word)
                #print(ourlist >> #1)
for lst in L:
    for word in lst:
        #started loop again for 3 time:
            for charachter in word:
                   if charachter == 'b':
                          b_strings.append(word)
                          break
print(b_strings)

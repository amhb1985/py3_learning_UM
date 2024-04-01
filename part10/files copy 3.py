

#Write code to find out how many lines are in the file emotion_words.
#txt as shown above. Save this value to the variable num_lines. 
#Do not use the len method.


#notice: we dont have this text file here!but we can use another text:
num_lines = 0

# Open the file
with open('emotion_words.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Increment the line count
        num_lines += 1

# Print the number of lines
print("Number of lines:", num_lines)
 # ok end 






# 10.08 Writing Text Files
#after running this code, part 1 and part 2 , we can see our file 
#with the name "squared_numbers" and with text format under the main folder

#part 1: 
for number in range(1, 13):
    square = number * number
    print(square)
    
#part 2.
filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()

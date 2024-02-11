#testing_another_txt_data
#part 1(it just show in Terminal): 
'''
for number in range(1, 5):
    square = number * 2
    print(square)
    '''
#part 2.(set and creat a file and then wirte in it)
filename = "number_x_2.txt"
outfile = open(filename, "w")

for number in range(1, 5):
    square = number * 2
    outfile.write(str(square) + "\n")

outfile.close()

'''
infile = open(filename, "r")
print(infile.read()[:10])
infile.close()
'''
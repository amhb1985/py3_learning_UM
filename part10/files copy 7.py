

#reading the text file and readline command 
fileref = open("olympics.txt", "r")
lines = fileref.readline()
for line in lines[:4]:
    print(line)
#print(lines[:4])
fileref.close()



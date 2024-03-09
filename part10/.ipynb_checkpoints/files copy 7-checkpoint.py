#reading the text file and readline command 
fileref = open("olympics.txt", "r")
lines = fileref.readline()
for lin in lines[:4]:
    print(lin)
#print(lines[:4])
fileref.close()

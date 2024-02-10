#another test for using "with" in one file:

with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
        
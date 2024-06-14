#the first thing in Working with Data Files is "reading file" :



#Note: cause of dont existing the olympics.txt here we can not see the result under the terminal
#fileref = open("info.txt", "r")

#fileref : (/workspaces/py3_learning_UM/part10/mydata.txt)
## other code here that refers to variable fileref
#fileref.close()

file_test_read = open("workspaces/py3_learning_UM/part10/mydata.txt","r")
print(file_test_read)
file_test_read.close()

#test
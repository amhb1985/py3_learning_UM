
#this is about the API
'''
#0 we must import 2 Majuls in this section
# the first one  REQUEST and 2nd one is JSON
import requests
import json
print("1st PART: ---------------------REQUEST-------------------------")

# 1.REQUEST  first we must set a variable as our URL (so it must be free) and then we must use the request.get("URL")
page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
#1.2 we can use the type() to see the Type of our page (varible)
print(type(page))
#1.3 we can see the first 150characters in our page
print(page.text[:150]) # print the first 150 characters

#1.4 with the page.url we can 
print(page.url) # print the url that was fetched

print("2nd PART: --------------------JSON---------------------------")

# 2.JSON :  in thsi part we use  a varilble as "x" to define a text file with commend.  page.json() to see use the text in pathon
x = page.json() # turn page.text into a python object
print(type(x))

'''
'''
this is the more info about json.dump():
json.dumps(): This function converts a Python object into a JSON string. The dumps() stands for "dump string".
It takes a Python object (like a dictionary, list, etc.) as input and returns a string representing that object in JSON format.
x: This is the Python object you want to convert to JSON format.
indent=2: This is an optional parameter of the dumps() function. 
It specifies the number of spaces to use for each level of indentation in the output JSON string. 
In this case, indent=2 means that each level of the JSON hierarchy will be indented by 2 spaces, making the resulting JSON string more human-readable.

''''''
print("---first item in the list---")
# 3. in this part we can use the exact 
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results
'''
'''
#example 2:
#0. like anither we must set a majol as request.
import requests

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
#so 1. we create a valuable as kval_pairs and set it as {Dictioary} here the both of KEY and VALUE are String! 
kval_pairs = {'rel_rhy': 'funny'}
#so we can see the type of our valuble 
print("The type of our valuable is:  ",type(kval_pairs))

#2. we set another valuable to get a request form the Sourcs(as URL , aand set the params as our first valuable)
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
#3. print the first 150 charachter with our 2nd valuacle.
print(page.text[:150]) # print the first 150 characters
# print the url that was fetched
print(page.url) 
'''

#example 3: i this example we try to use one url as google.com to search two word for Violons and guitars
#noice becaus of some security reson we can not allow to our result
#0 import majule request
import requests

#1. cereate one valuble as d in {Dictionary} 
d = {'q': '"violins and guitars"', 'tbm': 'isch'}
#2. create the 2nd valable as result to get request = request.get( "URL", params=d) 
results = requests.get("https://google.com/search", params=d)
#print result.url
print(results.url)
print(results.text)


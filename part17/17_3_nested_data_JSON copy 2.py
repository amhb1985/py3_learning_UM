 
#JSON : Java Script Object Notaion
#its easy to wtite and edit 
import json 

a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)    #here we can see the '.loads()' as mean load the Object in to String

print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])

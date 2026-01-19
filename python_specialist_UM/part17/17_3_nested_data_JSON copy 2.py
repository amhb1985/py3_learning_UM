 
#JSON : Java Script Object Notaion
#its easy to wtite and edit 
'''
import json 

a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)    #here we can see the '.loads()' as mean load the Object in to String
print("------")
print(type(d))
print(d.keys())
print(d['resultCount']) # print(a_string['resultCount'])
'''
import json
#so now we can set a nested file in our List:
#1. we must define an object:
def pretty(obj):
    #2. we must set dumps():  Dump an Object in to String
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))



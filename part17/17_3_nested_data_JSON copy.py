 
#JSON : Java Script Object Notaion
#its easy to wtite and edit 
import json 

    #we can set the Nested data  to JSON : 
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))

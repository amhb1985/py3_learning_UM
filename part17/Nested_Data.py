
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
'''
'''
#first of all we can see the one element from the 
print(nested1[0])

#2. we can count the list with len()
print(len(nested1))
#3. we append and add another element in list with .append(['i'])
nested1.append(['i'])
'''
print("-------")
#we can see the all of the List:
print(nested1)
print("-------")

for L in nested1:
    print(L)

'''


info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
          # so next we wanna for example change all of colorto to 95
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }
#now after the set color we'll define the personal data and 
#another realated nested Data or list

#for our goel to change the color we can all of the item = 95
info['personal_data']['physical_features']['color'] = 95
color = info['personal_data']['physical_features']['color']
print(color)



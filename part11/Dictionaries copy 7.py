#the final exam for Dictionary:
'''
At the halfway point during the Rio Olympics, the United States had 70 medals,
Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals. Create a dictionary assigned to the variable medal_count with 
the country names as the keys and the number of medals the country had as each key’s value.

'''

#we can set a Dic list with combinition
#  Keys >> Str 
#  Value >> Int
medal_count = {
    "United States": 70,
    "Great Britain": 38,
    "China": 45,
    "Russia": 30,
    "Germany": 17
}
print(medal_count.values())


'''#2. Given the dictionary swimmers, 
add an additional key-value pair to the dictionary 
with "Phelps" as the key and the integer 23 as the value. Do not rewrite the entire dictionary.
'''


swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}

swimmers["Phelps"] = 23

print(swimmers)
#print (swimemrs["Phelps"])


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

The dictionary golds contains information about how many gold medals each country 
won in the 2016 Olympics. But today, 
Spain won 2 more gold medals. Update golds to reflect this information.

'''


golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

golds["Spain"] += 2

print(golds)

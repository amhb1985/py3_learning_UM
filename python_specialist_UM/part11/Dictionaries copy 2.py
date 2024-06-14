# the some sample is :
#we can set one key with one exact varible in the List:
#for example here  we can set some information for the agae of every animail of a zoo 
#with info as Integers valus:


zoo_list = {"cat":12, "dog":6, "elephant":23}
print(zoo_list["cat"])

#for another example we must notice that we can
#use another form with '':

#create a dictionary for next
olympics = {
    'gold' : 7,
    'silver' : 8,
    'bronze' : 6
}

#print al of the medals in olympics
print(olympics)

# for one exact key we can use this form:
print(olympics['gold'])

#for adding/updating a data to one key probably as integer or foloat 
#we can use this form:

#first we must crat or have a Dictionary List:
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}

#2. dann we must first choose or key and then we can put methamatics formula
swimmers['Phelps'] =  swimmers['Phelps'] + 5

#3. at end we can see the reults:
print(swimmers)

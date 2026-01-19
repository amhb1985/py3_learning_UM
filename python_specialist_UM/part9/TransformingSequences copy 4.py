#testing againg with another example and tests:


#test with name and scre and print it in last 
#please Note to set str (string) command for score!
name = "Amir Habibi"
score = 1  # No respect!
print("Hello " + name + ". Your score is " + str(score))



#1.set score list:
scores = [("amir", 1), ("Marlon ", 3), ("eli", 4)]

#2.set one Loop for each element in list
for person in scores:
    name = person[0]
    score = person[1]
    print("Hallo " + name + ". Dein Punkt ist:  " + str(score))

    
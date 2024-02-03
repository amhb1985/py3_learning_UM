#testing againg with another example and tests:


#test with name and scre and print it in last 
#please Note to set str (string) command for score!
name = "Amir Habibi"
score = 1  # No respect!
print("Hello " + name + ". Your score is " + str(score))



#score and set info 
scores = [("amir", -1), ("Marlon ", 1), ("eli", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))
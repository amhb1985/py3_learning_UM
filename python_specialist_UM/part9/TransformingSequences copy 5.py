#another test:

scores = [("amir", -1), ("Marlon ", 1), ("eli", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))

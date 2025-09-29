#
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []

for word in words:
    if word.endswith("e"):
        past_tense.append(word + "d")
    else:
        past_tense.append(word + "ed")

print("Past tense words:", past_tense)

#exersize:
'''Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and corresponding letter grade, according to the table below.

Score
Grade
>= 90
A
[80-90)
B
[70-80)
C
[60-70)
D
< 60
F

'''

sc = input("Enter a score from 0 to 100 (decimal points are allowed)")
fl_sc = float(sc)

if fl_sc < 60:
    gr = "F"
elif fl_sc < 70:
    gr = "D"
elif fl_sc < 80:
    gr = "C"
elif fl_sc < 90:
    gr = "B"
else:
    gr = "A"

print("Score", fl_sc, "gets a grade of", gr)

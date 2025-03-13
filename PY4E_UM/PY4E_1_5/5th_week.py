
#thid is about the 5th week learning

#conditional Steps:
# if explain about the conditional situations
#changing for another Comparision Operators
'''
x = 2
if x == 5 :
    print("Equal5")

if x > 4 : 
    print("greater than 4.")
if x >= 5 : 
    print("Greater than or Equal 5. ")
if x < 6 :
    print("Less than 6")
if x <= 5 :
    print("Less than or Equal 5.")
if x != 6 :
    print("Not Equal 6.")


print("Finish!")

'''
'''
# and the now we speak about the Comparision Operators:
<   less than
<=  less than or Equal TimeoutError
==   Equal to 
>=  grater than or Equal 
>   greater than
!=  Not Equal 

= for the ASSIGMENT!
'''

#Notice: When start IF we must End it!

# Nested Decisions
'''
x = 42
if x > 1 : 
    print ('More than one')
    if x < 100 :
        print ('Less than 100')
print ('All done')
'''


# and now we try to test and lear else:
'''
y = 4
if y > 2 : 
    print ( 'Bigger')
else :
    print (' Smaller')
print( 'All done')
'''
# elif
# elif i sthe combination if and else :
'''x = 3
if x < 2 :
    print("smalll")
elif x < 10 : 
    print("Medium")
else : 
    print("Large.")
print ("all done")
'''


#answere the test with if and else:
#hrs = input("Enter Hours:")
#h = float(hrs)

# hours and coverst str to  float  
hours = input("Enter Hours: ")
hours = float(hours)

# rate (10.5) and coverst to Str to float  
rate = input("Enter Rate per Hour: ")
rate = float(rate)


# Calculate gross pay
if hours <= 40:
    pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * (rate * 1.5)
    pay = regular_pay + overtime_pay

# Print the result
print(pay)


#try and exept methode
# this is lik if else but in another form
'''
astr = "Bob"
try:
    print("Hello")
    istr = int(astr)
    print("There")
except:
    istr = -1
print("Done", istr)
'''
#0. input:
rawstr = input("Enter a Number:")

#1. try / except methode
'''
try:
    ival = int(rawstr)
except:
    ival = -1
#2. if / else methode:
if ival > 0 :
    print("Nice WOrk!")
else:
    print("Noth a Number.")


#the last test:
# Prompt the user for a score

score_input = input("Enter a score between 0.0 and 1.0: ")

try:
    # Convert the input to a float
    score = float(score_input)

    # Check if the score is within the valid range
    if score < 0.0 or score > 1.0:
        print("Error: Score is out of range.")
    else:
        # Determine the grade based on the score
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
        
        # Print the grade
        print(grade)

except ValueError:
    print("Error: Invalid input. Please enter a number between 0.0 and 1.0.")

'''

















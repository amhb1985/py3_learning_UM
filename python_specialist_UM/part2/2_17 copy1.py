#2.17. Exercises¶ in last part

''' 
challenge 1:
Challenge: Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. 
Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on the clock when the alarm goes off.
'''
# Ask the user : the current time
#we can input the current time
current_time = int(input("Wie spät ist jetzt? : "))

# Ask the user : the number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time using the 24-hour clock
alarm_time = (current_time + hours_to_wait) % 24

# Output the alarm time
print(f"The alarm will go off at {alarm_time}:00.")

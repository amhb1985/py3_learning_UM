'''
challenge2:
It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. 
If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return 
home after 10 nights you would return home on a Saturday (day 6). Write a general version 
of the program which asks for the starting day number, and the length of your stay, 
and it will tell you the number of day of the week you will return on.
'''
# Define the days of the week , we do not need the whole name of them
days_of_week = ["Su", "Mo", "Tu", "Wed", "Thu", "Fr", "Sa"]
days_of_Month = ["Su", "Mo", "Tu", "Wed", "Thu", "Fr", "Sa"]
# Ask the user for the starting day number (0 to 6)
start_day_number = int(input("Enter the starting day number (0 for Sunday, 1 for Monday, ..., 6 for Saturday): "))

# Ask the user for the length of stay
length_of_stay = int(input("Enter the length of your stay in nights: "))

# Calculate the return day number using the days_of_week list
return_day_number = (start_day_number + length_of_stay) % 7


# Output the day of the week you will return on
print(f"You will return home on a {days_of_week[return_day_number]}.")

# now at the end of the cours we'll try to add and use the jupter notbook(ipy)

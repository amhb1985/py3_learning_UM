#



#test 
'''
Implement the calculator for the date of Easter.

The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.

Ask the user to enter a year. Compute the following:
'''
#a = year % 19
#b = year % 4
#c = year % 7
#d = (19 * a + 24) % 30
#e = (2 * b + 4 * c + 6 * d + 5) % 7
#dateofeaster = 22 + d + e
#Special note: The algorithm can give a date in April. You will know that the date is in April if the calculation gives you an answer greater than 31. (You’ll need to adjust) Also, if the year is one of four special years (1954, 1981, 2049, or 2076) then subtract 7 from the date.

#Your program should print an error message if the user provides a date that is out of range.


def calculate_easter(year):
    if year < 1900 or year > 2099:
        print("Error: Year must be between 1900 and 2099.")
        return None
    
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date_of_easter = 22 + d + e
    
    # Check if the date is in April
    if date_of_easter > 31:
        date_of_easter -= 31
        month = "April"
    else:
        month = "March"
    
    # Check if it's a special year
    if year in [1954, 1981, 2049, 2076]:
        date_of_easter -= 7
    
    return f"Easter Sunday for the year {year} is on {month} {date_of_easter}."


# Input year from the user
year = int(input("Enter a year between 1900 and 2099: "))
print(calculate_easter(year))



'''
rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.

Hard-coded answers will receive no credit.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
'''
'''
# Split the string into a list of rainfall values
rainfall_values = rainfall_mi.split(", ")

# Initialize a counter for rainy months
num_rainy_months = 0

# Iterate through the rainfall values
for rainfall in rainfall_values:
    # Convert the rainfall value to a float
    rainfall_float = float(rainfall)
    # Check if the rainfall is greater than 3.0 inches
    if rainfall_float > 3.0:
        num_rainy_months += 1

print("Number of months with more than 3 inches of rainfall:", num_rainy_months)
'''
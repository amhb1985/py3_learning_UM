
'''
Challenge3: 
The formula for computing the final amount if one is earning compound interest is given on Wikipedia as

formula for compound interest
Write a Python program that assigns the principal 
amount of 10000 to variable P, assign to n the value 12, 
and assign to r the interest rate of 8% (0.08).
 Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.
'''
# Assign values to variables
P = 10000  # principal amount!
n = 12     # number of times interest is compounded per year
r = 0.08   # annual interest rate!

# Prompt user for  number of years
t = int(input("Enter the number of years: "))

# Calculate the final amount using the compound interest formula
A = P * (1 + r/n)**(n*t)

# Print the final amount after t years
print(f"The final amount after {t} years will be: {A:.2f}")

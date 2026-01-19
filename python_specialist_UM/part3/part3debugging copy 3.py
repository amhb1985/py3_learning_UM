# in this part we focus to the Debugging at the python script:

#you can see the error as 3.6. Runtime Errors:
'''
subtotal = input("Enter total before tax:")
tax = .08 * subTotal
print("tax on", subtotal, "is:", tax)
'''

#but the correct scripts is :
subtotal = int(input("Enter total before tax:"))
tax = 0.08 * subTotal
print("tax on", subtotal, "is:", tax)
# we can see the error as just simple mistake to input the number




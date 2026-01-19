#some test with input :
'''
person = input('Enter your name: ')
print('Hello {}!'.format(person))

'''

#set and calculate price and discount:

#1. set Price AND Discount >>> as Input and type as float:
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))

#2. Calculate new Price after discount
newPrice = (1 - discount/100)*origPrice

#3. Set an Explaination to show the result:
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)


#1 inputs:
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))

#2 formula & calculate:
newPrice = (1 - discount/100)*origPrice

#2. Eplaination
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)
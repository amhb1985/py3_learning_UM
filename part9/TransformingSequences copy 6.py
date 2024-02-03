#some test with input :
'''
person = input('Enter your name: ')
print('Hello {}!'.format(person))

'''

#set and calculate price and discount:

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)

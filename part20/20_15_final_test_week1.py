#this about the fin al test in first week:

# q 1:
'''
Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two
 instance variables, color and price. Assign to the variable testOne an instance of Bike whose color 
is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.

'''
'''
class Bike:
    def __init__(self,color,price):
        self.color=color
        self.price=price

testOne=Bike("blue",89.99)
testTwo=Bike("purple",25.0)
'''
#q2:Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a 
#quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called 
#increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of
# 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)
'''
class AppleBasket:
    def __init__(self,color,quant):
        self.apple_color=color
        self.apple_quantity=quant
        
    def increase(self):
        self.apple_quantity+=1
        return self.apple_quantity
    
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity,self.apple_color)

val1=AppleBasket('red',8)
print(val1)
print(val1.increase())
    ''' 
#q3:Define a class called BankAccount that accepts the name you want associated with your bank account in a string, 
#and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." 
#Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1.

# 0. first we need a claa as Bankacount
class BankAccount:
    #1. define init function (self, name, amt, acounts_cost)
    def __init__(self,name,amt, acountscost):
        self.name=name
        self.amt=amt
        self.acountscost = acountscost
    #2. define a string function
    #2.1 as you can see we can change the text with self
    def __str__(self):
        return "Hello {}. Your account as {}, has: {}$ .your acount cost is now: {}$. ".format(self.name, self.name,self.amt, self.acountscost)

#3. set 2 person info as name and amt infos   
#changing now to one input form

t0=BankAccount(input(str('whats your name: ')),100, 1)
t1=BankAccount("Bob",100, 1)
#t2=BankAccount("Joe",2000, 20)

print(t0)
#print(t2)


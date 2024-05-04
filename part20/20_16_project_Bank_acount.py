# this is about one example to show, connect to info bank and calculte the bank Commition.
# this one is base on the final Project of first Week exam in Py3 learining cours by UCLA Davis 
#under coursera website. 

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




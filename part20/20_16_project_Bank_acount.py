# this is about one example to show, connect to info bank and calculte the bank Commition.
# this one is base on the final Project of first Week exam in Py3 learining cours by UCLA Davis 
#under coursera website. 

# 0. first we need a class as Bankacount
class BankAccount:
    #1. define init function (self, name, amt, acounts_cost)
    def __init__(self,BankEmployee, AcountName, amt, percent, netto):
        self.employee = BankEmployee
        self.name = AcountName
        self.amt = amt
        self.percent= int(percent)*int(amt)/ 100
        netto = int(amt)-int(self.percent)
        self.netto = int(netto) 

        #self.percent= int(amt) * 0.01
    #2. define a string function
    #2.1 as you can see we can change the text with self
    def __str__(self):
        return "so.. dear {}.The account of {},now has: {}$ .The Bank-Comission cost is now: {}$. and the Net_Amount that add in Acount is: {} € ".format(self.employee, self.name,self.amt, self.percent, self.netto)

#3. set 2 person info as name and amt infos   
#changing now to one input form
#Notice i think we need exact 4 elemnt for each
t0=BankAccount(input(str('whats your name: '))
                ,input(str('whats acount name: '))
                  ,input(str('how much is payment: '))
                    ,input(str('please add Commition % : '))
                     ,'netto')
input(str('do you want to save it?'))

#t1=BankAccount("Bob",100, 1)
#t2=BankAccount("Joe",2000, 20)


print(t0)
#print(t2)
#just learn it again

#ok

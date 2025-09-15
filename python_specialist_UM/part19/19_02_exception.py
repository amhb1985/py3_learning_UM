
#so in this py code wewill see the Index Error after running the code:
# so now if we crrect or Item with add 3'd item in our List we can see a b and without somthing Wrong!
items = ['a', 'b','c']
#print("this is not going to be printed")

#so now we try to show the last print if the code it will not true:
#actually this is a Boolan inside of our code
#01. use try: and then except: third = False

#so now we can show or set where that we can problem: with 3 diffrent Print()
try:
    print("a")
    third = items[2]
    print("b")

except:
    print("Something went Wrong!")
    third = False
print("I wanna this to run")

#after running the code we can see as below:
#IndexError: list index out of range
#its mean that we have error because we had just 2 item in our list NOT 3!

#as we can see we have three Error when we have mistake:
#1. Syntadic >> like a () or []
#2.Runtime >>. like a item out of our List 
# for this one we can use the try/except 
#3.Semantic >>

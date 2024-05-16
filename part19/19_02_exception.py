
#so in this py code wewill see the Index Error after running the code:
#
items = ['a', 'b']
#print("this is not going to be printed")

#so now we try to show the last print if the code it will not true:
#actually this is a Boolan inside of our code
#01. use try: and then except: third = False
try:
    third = items[2]

except:
    third = False
print(" i wanna this to run")

#after running the code we can see as below:
#IndexError: list index out of range
#its mean that we have error because we had just 2 item in our list NOT 3!

#as we can see we have three Error when we have mistake:
#1. Syntadic >> like a () or []
#2.Runtime >>. like a item out of our List
#3.Semantic >>

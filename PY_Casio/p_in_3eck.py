
#dies ist fuer p
#Rechtwinkel Dreieck

# sollte naturlisch in der TR mit 
#Symbole erklaeren lassen
import math
a = float(input("enter a = "))
b = float(input("enter b = "))
c = float(input("enter grosse c = "))

p=((b**2+c**2)-(a**2))/(2*c)
h =math.sqrt((b**2)-(p**2))

print("p=(b²+c²)-(a²)/2.c")
#print("p=(b2 +a2)/2*c")
print("p ist: ",p)

print("h=Sqr Γ(b²-p²)")
#print("h=sqrt(b2-p2)")
print("h ist: ",h)

#ende


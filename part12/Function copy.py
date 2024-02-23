


#
'''def addit(x):
    return x + 5

def mult(x):
    return x * addit(x)

# Example usage:
result = mult(3)
print(result)  # Output will be 24

'''
'''
def pow(b, p):
    y = b ** p
    return y



def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)
'''

#What will the following code output?


#First square 2, then add 3.
'''def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print(h(2))
'''

#q2_whats the answer?

def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

#✔️ h(2) returns 7, so y is bound to 7 when g is invoked.
print (g(h(2)))

      

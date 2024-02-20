

#test

'''
def square(x):
    y = x * x
    return y

print(square(square(2)))
'''

#Annotations

def duplicate(msg: str) -> str:
    """Returns a string containing two copies of `msg`"""

    return msg + msg

result = duplicate('Hello ... ')
print(result)
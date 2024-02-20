

#test

'''
def square(x):
    y = x * x
    return y

print(square(square(2)))
'''

#Annotations

# we create one Function with the some index commend for example here will : " duplicate "
# and then we wil try set an exact type to our Function inside of ()

'''def duplicate(msg: str) -> str:
    """Returns a string containing two copies of `msg`"""

    return msg + msg

result = duplicate('Hello ... again ->  ')
print(result)
'''
'''
def add(x: int, y: int) -> int:
    """Returns the sum of `x` and `y`"""

    return x + y

def get_number(msg: str) -> float:
    """Prompts with `msg` for input; returns numeric response."""

    return float(input(msg))

def display_msg(msg: str):
    """Displays `msg` with dashed line underneath"""

    print(msg)
    print('-------------------------------------')


'''

#test to input
#display = input("write your Number:")
def display(msg: str):
    """Displays `msg` on the screen"""
    print(msg + 2)

display()

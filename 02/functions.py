# functions In python do not suffer HOISTING

def say_hi(phrase, optional = 'Im optional!'):
    print(phrase)
    print(optional)

say_hi('Hello World')
say_hi('This Is', 'cool!')


def cube_number(num):
    cubed = pow(num, 3)
    return cubed

cubed = cube_number(3)
print(cubed)
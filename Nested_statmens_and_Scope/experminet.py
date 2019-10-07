x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

# Local variable num

print(list(map(lambda num: num ** 2, [1, 2, 3])))

#GLOBAL
name = 'This is a global string'


def greet():
    # ENCLOSING
    name = 'Sammy'

    def hello():
        # LOCAL
        name = 'I am a local'
        print('Hello ' + name)
    hello()


greet()

x = 50


def func():
    global x
    print(f'X is {x}')

    # Local reassigment
    x = 'New value '
    print(f'I just locally change x to {x}')


print(func())
print(x)
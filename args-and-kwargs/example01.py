def myfunc(a, b):
    # Returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


print(myfunc(40, 60))


def myfunc01(*args):
    return sum(args) * 0.05


print(myfunc01(10, 5, 20))


def myfunc02(*args):
    for item in args:
        print(item)


myfunc02(5, 6, 7, 8)


def myfunc03(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))


myfunc03(fruit='apple')


def myfunc04(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc04(10, 20, 30, fruit='orange', food='eggs', animal='god')


def myfunc05(*args):
    for item in args:
        if item % 2 == 0:
           print(item)


print(myfunc05(5, 6, 7, 8))

# Correct


def myfunc(*args):
    list=[num for num in args if num % 2 == 0]
    return list


print(myfunc(5, 6, 7, 8))


def myfunc00(*args):
    for letter in range(len(args)):
        if letter % 2 == 0:
            return(str)


print(myfunc00("adadsadada"))

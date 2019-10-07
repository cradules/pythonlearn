def ran_check(num, low, high):
    if num in range(low, high+1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')


print(ran_check(5, 2, 7))


def ran_check_bol(num, low, high):
    if num in range(low, high+1):
        return True
    else:
        return False


print(ran_check_bol(5, 2, 7))


def ran_check_bol_simple(num, low, high):
    return num in range(low, high+1)


print(ran_check_bol_simple(5, 2, 7))

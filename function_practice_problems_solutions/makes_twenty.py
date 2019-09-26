def makes_twenty(n1, n2):
    # if n1 + n2 == 20:
    #     return True
    # elif n1 == 20:
    #     return True
    # elif n2 == 20:
    #     return True
    # else:
    #     return False
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20


print(makes_twenty(10, 10))
def count_primes(num):
    # Check for 0 and 1
    if num < 2:
        return 0
    ###############
    # 2 or greater
    ##############
    primes = [2]
    # Counter up to input num
    x = 3
    # x is going through every number up to input num
    # Check if x is prime
    while x <= num:
        # for y in range(3, x, 2):
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    # return len(primes)
    print(len(primes))


count_primes(5)
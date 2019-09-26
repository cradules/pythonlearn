def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # BOTH NUMBERS ARE EVEN
        return min(a, b)
    else:
        # One or both numbers are odd
        return max(a, b)


print(lesser_of_two_evens(5, 3))

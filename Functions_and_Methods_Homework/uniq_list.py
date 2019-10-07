def unique(lst):
    x = []
    for num in lst:
        if num not in x:
            x.append(num)
    return x


print(unique([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

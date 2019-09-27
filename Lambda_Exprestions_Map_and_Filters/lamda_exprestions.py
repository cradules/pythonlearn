# Example 1
# def square(num):
    # result = num ** 2
    # return num ** 2

# Example 2
# def square(num): return num ** 2

# Lamda function



#lambda num: num ** 2

#Square
mynums = [1, 2, 3, 4]
print(list(map(lambda num: num ** 2, mynums)))
for y in list(map(lambda num: num ** 2, mynums)):
    print(y)

#Even Numbers
print(list(filter(lambda num: num % 2 == 0, mynums)))
for y in filter(lambda num: num % 2 == 0, mynums):
    print(y)

names = ['Vali', 'Bianca', 'Maia']
print(list(map(lambda x: x[::-1], names)))




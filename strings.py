# Strings Immutability

name = "Sam"

# The strings cant me mutate. Check commented below example
# name[0] = 'P'

last_letters = name[1:]
print(name)
print(last_letters)

print('P' + last_letters)

x = "Hello World"
print(x + ' it is beautiful out side!')
x = x + ' it is beautiful out side!'
print(x)

# Multiplication

letter = 'z'
print(letter * 10)


# Numbers

print(2 + 3)
print('2' + '3')

# NOT!
# print(2 + '3')

# Method

x = 'Hello World'
print(x.upper())
print(x.split())
print(x.split('o'))

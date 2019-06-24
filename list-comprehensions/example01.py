mystring = 'hello'

mylist = []

for letter in mystring:
    mylist.append(letter)
print(mylist)

# Efficient way
mylist = [letter for letter in mystring]
print(mylist)

# Some other example

mylist = [x for x in 'word']
print(mylist)

mylist = [num**2 for num in range(0, 11)]
print(mylist)

# if statmes

mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)

# Tempeture

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

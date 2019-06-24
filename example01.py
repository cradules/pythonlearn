# Iterate form 0 to 9 using range
print("First iterate")
for num in range(10):
    print(num)

# Iterate from 3 up 10 but not including 10
print("Second iterate")
for num in range(3, 10):
    print(num)

# Create list using range generator
print(list(range(0, 11, 2)))


# Enumerate function
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word='abcde'
for item in enumerate(word):
    print(item)

# Check if something in a list
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])

print('mykey' in {'mykey': 345})

# Check min and max
alist = [10, 20, 30, 40, 50, 60]
print(min(alist))
print(max(alist))
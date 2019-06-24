my_list = [1, 2, 3]

for y in range(10):
    print(y)


my_list = list(range(10))

print(my_list)

# Enumarate

index_count = 0

for y in 'abcde':
    print('At index {} the letter is {}'.format(index_count, y))
    index_count += 1


word = 'abcde'

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')


my_list01 = list(range(1, 4))
my_list02 = ['a', 'b', 'c']

for y in zip(my_list01, my_list02):
    print(y)

print('END')

for y, z in zip(my_list01, my_list02):
    print(y)
    print(z)
    print('\n')
print('END')

'x' in [1, 2, 3,]
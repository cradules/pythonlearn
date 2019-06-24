mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for y in mylist:
# #     print(y)
# #     print('hello')
# # =============

for y in mylist:
    # Check if the number are even
    if y % 2 == 0:
        print(f'Even number {y}')
    else:
        print(f'Odd number{y}')

list_sum = 0
for y in mylist:
    list_sum = list_sum + y
    print(list_sum)
print(list_sum)

mystring = 'Hello World'

for y in mystring:
    print(y)

my_list2 = [(1, 2), (3, 4)]

for y in my_list2:
    print(y)
for (y, z) in my_list2:
    print(y)
    print(z)

d = {'k1': 1, 'k2': 2, 'k3': 3}


for y in d:
    print(y)
for y in d.items():
    print(y)
for key, value in d.items():
    print(value, key)
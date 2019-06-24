# import os
#
# dir_path = os.getcwd()
# my_file = open('my_file.txt')
# print('My current path is ' + dir_path)
#
#
# print(my_file.read())
# print(my_file.read())
# my_file.seek(0)
#
# print(my_file.read())
#
# my_file.seek(0)
#
# print(my_file.readlines())
#
#
# # Open a file in safe way
# with open('my_file.txt') as my_new_file:
#     contents = my_new_file.read()
#     name = my_new_file.name
# print(contents)
# print(name)


# with open('my_new_file.txt', mode='r') as f:
#     print(f.read())
#
# my_file = 'my_new_file.txt'
# with open(my_file, mode='a') as f:
#     f.write('\nFOUR ON FOURTH')
# with open(my_file) as f:
#     print(f.read())

my_w_file = 'dada.txt'

with open(my_w_file, mode='r+') as f:
    f.write('\nTHIS IS A NEW LINE')
    print(f.read())


with open('test.txt', mode='w') as f:
    f.write('Hello World')
my_list = [1, 2, 3]

my_list= ['STRING', 100, 23.2]

print(len(my_list))

my_list = ['one', 'two', 'three']

print(my_list[0])
print(my_list[1:])

another_list = ['four', 'five']

print(my_list + another_list)

new_list = my_list + another_list

print(new_list)

new_list[0] = 'ONE ALL CAPS'

print(new_list)

new_list.append('six')

new_list.pop()

print(new_list)
popped_item = new_list.pop()
print(popped_item)

print(new_list)

print(new_list.pop(2))

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

new_list.sort()

print(new_list)

num_list.sort()

print(num_list)
num_list.reverse()

print(num_list)
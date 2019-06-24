x = 0

while x < 5:
    print(x)
    x += 1


x = [1, 2, 3]
for y in x:
    # comment
    pass
print('end of my script')


my_string = 'Sammy'

for y in my_string:
    if y == 'a':
        continue
    print(y)
print('END')

for y in my_string:
    if y == 'a':
        break
    print(y)
print('END')
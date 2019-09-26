def master_yoda(text):
    word_list = text.split()
    reverse_word_list = word_list[::-1]
    return ' '.join(reverse_word_list)


print(master_yoda('I am home'))
print(master_yoda("We are ready"))

# Joining a list

mylist = ['a', 'b', 'c']
print('--'.join(mylist))

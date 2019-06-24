# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

for letter in st.split():
    if letter[0] == 's':
        print(letter)

# Use range() to print all the even numbers from 0 to 10.

print(list(range(0, 11, 2)))

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

print([x for x in range(1, 51) if x % 3 == 0])


# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 == 0:
        print(word+"<---EVEN")
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1, 101):
    if x %3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Frizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
for word in st.split():
    print(word[0])
print([word[0] for word in st.split()])

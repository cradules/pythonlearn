# Function

def name_of_the_function():
    """
    Docstring explains function
    :return:
    """
    print("Hello")
# Function ca take parameters


def with_par(name):
    """
    Docstring explains function
    :return:
    """
    print("Hello" + name)


print(name_of_the_function())
print(with_par("Vali"))

# Use return insted of print


def add_function(num1, num2):
    return num1 + num2


result = add_function(1, 2)

print(result)


def name_function():
    """
    INPUT: no input
    OUTPUT: Print Hello...
    :return:
    """
    print("Hello name_function")


def say_hello(name='Name'):
    return "Hello_say_hello " + name


result = say_hello("Jop")
print(result)


def add(n1, n2):
    return n1 + n2


result = add(1231231313, 2323213213)
print(result)


# Find out if the word dog is in a string

def dog_check(mystring):
    return 'dog' in mystring.lower()


print(dog_check('Dog ran away'))


#PIG LATING
# If word starts with a vowel, add 'ay' to end
# If word dose not start with a vowel, put first letter at the end, then add 'ay'
# word --> ordway
# word --> appleay

def pig_latin(word):
    first_letter = word[0]

    # Check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin('word'))
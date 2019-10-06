import string


# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4 / 3) * 3.14 * (rad ** 3)


print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    # Check if num is between low and high (including low and high)
    if num in range(low, high + 1):
        print('{} is in range between {} and {}'.format(num, low, high))
    else:
        print('The number is out of range')


# Write a function that checks whether a number is in a given range (inclusive of high and low) boolean
def ran_check_bol(num, low, high):
    if num in range(low, high):
        return True
    else:
        return False


ran_check_bol(5, 2, 7)
ran_check(5, 2, 7)


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original string: ", s)
    print("No. of Upper case characters: ", d["upper"])
    print("No. of Lower case characters: ", d["lower"])
    print("No. of total case characters are: ", d["upper"] + d["lower"])


up_low("Hello Mr. Rogers, how are you this fine Tuesday?")


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply([1, 2, 3, -4]))


# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(s):
    s = s.replace(' ',
                  '')  # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have  spaces)
    return s == s[::-1]  # Check through slicing


print(palindrome('nurses run'))


# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(ispangram("The quick brown fox jumps over the lazy dog"))

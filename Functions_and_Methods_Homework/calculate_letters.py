def up_low(s):
    d = {"upper": 0, "lower": 0}
    for letter in s:
        if letter.isupper():
            d['upper'] += 1
        elif letter.islower():
            d["lower"] += 1
        else:
            pass
    print('Original String : ', s)
    print('No. of Upper case characters: ', d["upper"])
    print('No. of lower case characters: ', d["lower"])


print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

import string


def ispangram(line, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(line.lower())

print(ispangram('The quick brown fox jumps over the lazy dog'))
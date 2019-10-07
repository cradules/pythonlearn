# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


print(palindrome('nurses run'))

## Level 0
# a = 2**38
#
# print(a)

def alphaDecoder(string):
    code = list(string)
    newCode = ''

    for i in code:
        if i.isalpha():
            newCode += chr(ord(i)+2)
        else:
            newCode += i

    return newCode

word = input('Enter String here: ')
print(alphaDecoder(word))


# raw = "http://www.pythonchallenge.com/pc/def/map.html"
#
# table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
#
# result = raw.translate(table)
#
# print(result)
#


# Challenge 2 Finding the rare one:

# from collections import Counter
#
# String = input('Enter the String here: ')
#
# coded = Counter(String)
#
# print(coded)

#Counter({'-': 2, '<': 1, '!': 1})
#Given a string of alphabetical characters - rearrange them to be alphabetical
# A) String contains no upper case
# B) String contains upper case

# a = 'string'
# print(''.join(sorted(a)))


# def alphabetSoup(string):
#     li = sorted(list(string))
#     newString = ''
#     for char in li:
#         newString += char
#     return newString
#
# word = input('Please Enter a String: ')
# print(alphabetSoup(word))

# Part B  - alphabetize the string w/ upper and lower case character

def alphabetSoup(string):
    li = sorted(list(string))
    lowerLi = sorted(list(string.lower()))
    caps = []
    newString = ''

    for char in li:
        if char.isupper():
            caps.append(char)

    for letter in lowerLi:
        if caps.count(letter.upper()) != 0:
            newString += letter.upper()
            caps.pop(caps.index(letter.upper()))
        else:
            newString += letter
    return newString

word = input('Please Enter String here: ')
print(alphabetSoup(word))


a = 2**38
print(a)
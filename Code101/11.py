# accept a string and calculate number of letter and digits

s = input('give me a string : ')
l, d, k= 0, 0, 0
for c in s:
    if c.isalpha():
        l= l +1
    elif c.isdigit():
        d = d +1
    else:
        k = k +1
print('# of letters: ',l)
print('# of numbers: ',d)
print('# of other: ',k)

# at least 1 number [0-9]
# at least 1 character[$#@]
# min 6 and max 16 character

import re # re = regular expression matching operations

p = input('enter password: ')
x = True
while True:
    if (len(p)< 6 or len(p)>16):
        break
        #password needs to be minimum 6 and maximum 16 characters
    elif not re.search('[a-z]', p):
        break
        #please add alphanumric character to your password
    elif not re.search('[0-9]', p):
        break
        #please add alphanumric character to your password
    elif not re.search('[A-Z]', p):
        break
        #add an upper.alphanumeric character
    elif not re.search('[$#@]', p):
        break
        #please add the following to your password $#@
    elif re.search('\n', p):
        break
        #no white space
    else:
        print('password checks out')
        x = False
        break
if x:
    print('that is a bs password - you are banned for life')

# find numbers between 100 and 400(both included, where each digit is even
# print in csv sequence

even_digits = []
for i in range(100,401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        even_digits.append(s)
print(' $ '.join(even_digits))

# create a program that will pirnt out a pattern of an 'A'

letter_A = ''
for row in range(0,7):
    for column in range (0,7):
        if(((column == 1 or column ==5) and row !=0) or ((row==0 or row==3) and (column>1 and column <5))):
            letter_A = letter_A + '*'
        else:
            letter_A = letter_A + ' '
    letter_A = letter_A + '\n'
print(letter_A)
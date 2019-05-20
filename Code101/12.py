# make a grid an find out how to move the dots to the right to make it an s
#lets do the same for 's' its good practice

# letter_s = ''
# for row in range(7):
#     for col in range(7):
#         if((row == 0 or row == 3 or row == 6) and col>0 and col<7):
#             letter_s = letter_s + '*'
#         elif ((row == 1 or row == 2) and col == 1):
#             letter_s = letter_s + '*'
#         elif ((row == 4 or row == 5) and col ==6):
#             letter_s = letter_s + '*'
#         else:
#             letter_s = letter_s + ' '
#     letter_s = letter_s + '\n'
# print(letter_s)

# craeting an 'x'

# x= ""
# for row in range(0,7):
#     for column in range(0,7):
#         if (((column ==1 or column ==5) and (row > 4 or row < 2)) or row == column and column > 0 and column < 6 or (column == 2 and row ==4) or (column ==4 and row ==2)):
#             x = x + 'x'
#         else:
#             x = x + ' '
#     x = x + '\n'
# print(x)

# python program which calculates age in dog years
# dog years from 0 - 2 = 10.5 human years for each year
# after that each dog year = 4 human years

# human  = int(input('how many human years has the dog been alive? '))
# if human < 0:
#     print('age must be a positive number')
#     exit()
# elif human <= 2:
#     dog_age = human * 10.5
# else:
#     dog_age = 21 + (human -2) * 4
# print("the dog's age in dog's year is :", dog_age)

# python program to check if letter is a vowel or a consonant

# i = input('Choose any letter from the alphabet: ')
# for x in i.lower():
#     if x in('a', 'e','i','o','u','y'):
#         print('{} is a vowel'.format(x))
#     else:
#         print('{} is a consonant: '.format(x))

# give me a month and i'll share the number of days

months = ['January', 'February', 'March', 'April', 'May','June','July','August','September','October','November','December']
print('List of Months: ', months)
month = input('Give me a month: ')
if month == 'February':
    print('There are either 28 or 29 days in the month of {}'.format(month))
elif month in ('April', 'June', 'September', 'November'):
    print('There are 30 days in the month of {}'.format(month))
elif month in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
    print('There are 31 days in the month of {}'.format(month))
else:
    print('type of the month better!')

# could have created a dictionary for each month and do a call
# instead of creating a if statement
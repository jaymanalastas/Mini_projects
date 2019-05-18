# allow 2 inputs, month and day and program can spit out season
# month = input('Type in a month: ')
# day = int(input('select a numerical day: '))
#
# x = ['January', 'February', 'March']
# y = ['April', 'May', 'June']
# z = ['July', 'August', 'September']
#
# if month in (x):
#     season = 'winter'
# elif month in (y):
#     season = 'spring'
# elif month in (z):
#     season = 'summer'
# else:
#     season = 'autumn'
#
# if (month == 'March') and (day > 19):
#     season = 'spring'
# elif (month == 'June') and (day > 20):
#     season = 'summer'
# elif (month == 'September') and (day >21):
#     season = 'autumn'
# elif (month == 'December') and (day > 20):
#     season = 'winter'
#
#
# print('Season is, {}'.format(season))

# give me date of birth and I will give you your sign
month = input('Input birth month: ')
day = int(input('Input birth day: '))

if month == 'December':
    sign = 'Sagittarius' if day < 22 else 'Capricorn'
elif month == 'January':
    sign = 'Capricorn' if day < 20 else 'Aquarius'
elif month == 'February':
    sign = 'Aquarius' if day < 20 else 'Pisces'
elif month == 'March':
    sign = 'Pisces' if day < 20 else 'Aries'
elif month == 'April':
    sign = 'Aries' if day < 20 else 'Taurus'
elif month == 'May':
    sign = 'Taurus' if day < 20 else 'Gemini'
elif month == 'June':
    sign = 'Gemini' if day < 20 else 'Cancer'
elif month == 'July':
    sign = 'Cancer' if day < 20 else 'Leo'
elif month == 'August':
    sign = 'Leo' if day < 20 else 'Virgo'
elif month == 'September':
    sign = 'Virgo' if day < 20 else 'Libra'
elif month == 'October':
    sign = 'Libra' if day < 20 else 'Scorpio'
elif month == 'November':
    sign = 'Scorpio' if day < 20 else 'Sagittarius'

print('Your sign from the stars is: ', sign)
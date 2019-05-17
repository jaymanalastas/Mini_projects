# allow 2 inputs, month and day and program can spit out season
month = input('Type in a month: ')
day = int(input('select a numerical day: '))

x = ['January', 'February', 'March']
y = ['April', 'May', 'June']
z = ['July', 'August', 'September']

if month in (x):
    season = 'winter'
elif month in (y):
    season = 'spring'
elif month in (z):
    season = 'summer'
else:
    season = 'autumn'

if (month == 'March') and (day > 19):
    season = 'spring'
elif (month == 'June') and (day > 20):
    season = 'summer'
elif (month == 'September') and (day >21):
    season = 'autumn'
elif (month == 'December') and (day > 20):
    season = 'winter'


print('Season is, {}'.format(season))
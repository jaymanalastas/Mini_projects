# reverse an input str

x = input('Type what you want to reverse...')
b = ''.join(reversed(x))
print(b)
# or, use a start end step, slices str steps -1

print(x[::-1])

# count even or odd from a series of numbers

def oddEvenCount(x):
    odd_count = 0
    even_count =0
    for i in x:
        if i % 2 ==0:
            even_count += 1
        else:
            odd_count += 1
    return "odd count: "+ str(odd_count) + "\neven count: "+ str(even_count)

x = [1,2,3,4,5,6,7,8,9,10,11]
print(oddEvenCount(x))

# given the below list, print out the item and its type

data = [1452, 11.23, 1+2j, True, 'w3resource', (0.-1), [5,12], {'class':'V', 'section':'A'}]


for icecream in data:
    print('Type of ', icecream, ' is ', type(icecream))

#write program prints all numbers except 3 and 6

for i in range(7):
    if i != 3 and i != 6:
        print(i)
print('\n')

# write a program iterating 0 to 50. If um is multiple of 3 print SUPAA
#if num is multiple of 5 print BADASS. If num is multiple of both print Suppa badass

for moomoo in range(1,50):
    if moomoo%3==0 and moomoo%5==0:
        print('SUPPA BADASS!!')
    elif moomoo % 5 ==0:
        print('BADASS')
    elif moomoo % 3 ==0:
        print('SUPAA')
    else:
        print(moomoo)

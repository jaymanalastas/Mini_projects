# given integral number n, create a dictionary with the function that creates the squre of our n
# integral is a number assigned to a function


print('Enter an int: ')
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i**2
print(d)


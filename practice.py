# 1 create a list from an if statement

# empty_list = []
# for i in range(200, 400):
#     if (i%7==0) and (i%5!=0):
#         empty_list.append(str(i))
# print(', '.join(empty_list))

#2 factorials of of a number input

# def factorials(num):
#     if num ==0:
#         return 1
#     return num * factorials(num-1)
# print('Enter int here: ')
# num = int(input())
# print(factorials(num))

#3 create a dictionary - of square

#
# n = int(input('Enter an int here: '))
# d = dict()
# for i in range(1, n+1):
#     d[i] = i**2
# print(d)


#4 Cs numbers for both tuple and list

# values = input('Enter a cs numbers here: ')
# l = values.split()
# d = tuple(l)
# print(l,d)


#5 Class Mama

# class Mama(object):
#     def __init__(self):
#         self.s = ''
#     def getString(self):
#         self.s = input('Input any strings here: ')
#     def printString(self):
#         print(self.s.upper())
#
# x = Mama()
# print(x)
# x.getString()
# x.printString()


#6 # use this formula Q = square root of [(2*c*d)/h] c = 50 h= 30

c = 50
h = 30

import math

x = []
y =[i for i in input('Enter int here: ').split(',')]
for d in y:
    x.append(str(int(round(math.sqrt((2*c*float(d))/h)))))
print(','.join(x))

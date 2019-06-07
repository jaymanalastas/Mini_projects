# 1 create a list from an if statement

# empty_list = []
#
# for i in range(400,500):
#     if (i%7 ==0) and (i%5!=0):
#         empty_list.append(str(i))
#     print(' '.join(empty_list))

#2 factorials of of a number input

# def factorial(num):
#     if num ==0:
#         return 1
#     return num * factorial(num-1)
# print("please input a int: ")
# num = int(input())
# print(factorial(num))

#3 create a dictionary - of square

# n = int(input('Please Enter String here: '))
# d = dict()
# for i in range(1, n+1):
#     d[i] = i**2
# print(d)


#4 Cs numbers for both tuple and list

# values = input('Enter a number that is cs: ')
# a = values.split()
# b = tuple(a)
# print(a,b)

#5 Class Mama (Creating an Upper case String)

# class Mama(object):
#     def __init__(self):
#         self.s = ''
#     def getString(self):
#         self.s = input('Enter String here: ')
#     def printString(self):
#         print(self.s.upper())
#
# x = Mama()
#
# x.getString()
# x.printString()

#6 # use this formula Q = square root of [(2*c*d)/h] c = 50 h= 30

# c = 50
# h =30
#
# import math
# x = []
# y = [i for i in input('Enter int here: ').split(',')]
# for d in y:
#     x.append(str(int(round(math.sqrt((2*c*float(d))/h)))))
# print(x)


#7 take 2 digits, x and y as inputs and generate 2 dimensional arry

# input_for_system = input('Enter two int to form two dimensional array: ')
# dimension = [int(x) for x in input_for_system.split(',')]
# rowin = dimension[0]
# colin = dimension[1]
# list = [[0 for col in range(colin)] for rows in range(rowin)]
#
# for row in range(rowin):
#     for col in range(colin):
#         list[row][col]= row*col
# print(list)

#
#Alphabet Soup


def not_string(str):
  newString = ''
  for i in str():
    if i != 'n':
      newString.appened('not ' + str)
    else:
      newString += str()
  print(newString)
word = input('Please Enter String here:')

print(not_string(word))
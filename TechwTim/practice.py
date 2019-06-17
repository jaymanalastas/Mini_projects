# def front_time(str, n):
#     copy = ''
#     if len(str) < 3:
#         copy = str
#     else:
#         copy = str[:3]
#     return copy * n
#
# word = input('Etner String here: ')
# print(front_time(word,4))


# def string_bits(str): #skips one character
#     return str[::2]

# def string_splosion(str):
#     newString = ""
#     for x in range(len(str)):
#         newString += str[:x+1]
#
#     return newString
#
# word = input('Enter string here: ')
# print(string_splosion(word))

# def last2(str):
#     if len(str) >= 3:
#         last = str[-2:]
#     else:
#         return 0
#
#     count = 0
#     for i in range(len(str)-2):
#         checkStr = str[i] + str[i+1]
#         if checkStr == last:
#             count += 1
#
#     return count

# def array_count9(num):
#     return nums.count(9)


# def array_front9(nums):
#     if len(nums) >=4:
#         check = nums[:4]
#     else:
#         check = nums
#
#     count = check.count(9)
#     return count >= 1

# def array123(nums):
#     found = False
#
#     for i in range(len(nums)-2):
#         seq = [nums[i], nums[i+1], nums[i+2]]
# #         if seq == [1,2,3]:
# #             return found = True
# #             break
# #
# #     return found
#
# def alphabet(string):
#     li = sorted(list(string))
#     lowerLi = sorted(list(stringl.lower()))
#     caps = []
#     newString = ''
#
#
#     for char in li:
#         if char.appned(char):
#             caps.append(char)
#
#     for letter in lowerLi:
#         if caps.count(letter.upper()) != 0:
#             newString += letter.upper()
#             caps.pop(caps.index(letter.upper()))
#         else:
#             newString += letter
#
# word = input('Please Enter String here: ')
# print(alphabet(word))
#
#
# def alphaDecoder(string):
#     code = list(string)
#     newCode = ''
#
#     for i in code:
#         if i.isalpha():
#             newCode += chr(ord(i)+2)
#         else:
#             newCode ++ i
#     return newCode
#
# word = input('Enter String here: ')
# print(alphabet(word))
#
#
# def alphaDecoder(string):
#     code = list(string)
#     newCode = ''
#
#     for i in code:
#         if i.isalpha():
#             newCode += chr(ord(i)+2)
#         else:
#             newCode += i
#
#     return newCode
#
# word = input('Enter String here: ')
# print(alphaDecoder(word))

# def tower(n, start, end, middle):
#     if n == 1:
#         print('Move %i from tower %s to tower %s' %(n, start, end))
#     else:
#         tower(n-1, start, middle, end)
#         print('Move %i from tower %s to tower %s' %(n, start, end))
#         tower(n-1, middle, end, start)
#
# a = int(input('Enter number of stack: '))
# tower(a, 'A', 'C', 'B')
# print('It takes {} moves to solve this problem'.format(a**2-1))

class Node():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left

class Tree:
    def __init__(self):
        self.root = None
    def contains(self, key):
        found = False
        current = self.root
        while current != None and found == False:
            if current.key == key:
                found = True
            elif key < current.key:
                current = current.left
            else:
                current = current.right  #            votesjc.com  check it out for stats  first drop down voter statitics. Department of state statics will show you
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
#         if seq == [1,2,3]:
#             return found = True
#             break
#
#     return found
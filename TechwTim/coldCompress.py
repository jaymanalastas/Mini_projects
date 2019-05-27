#GET INPUT FROM LINE

# n = int(input())
# lines = []
#
#
# for _ in range(n):
#     lines.append(input())


#GET INPUT FROM TEXT FILE

with open(r"C:\Users\14078\PycharmProjects\Mini_projects\TechwTim\sampleInput.txt", "r") as f:
    lines = f.readlines()

# SOLVE PROBLEM


# for line in lines[1:]:  # For each input
#     line = line.strip() # Remove \n from each line
#
#     newStr = ""
#     last = line[0]
#     count = 1
#
#     for char in line[1:]:  #for every character except the first (because we already handled it above)
#
#         if char == last:  # if the next character is equal to the last (consecutive chars)
#             count += 1
#
#         else:  # If the next character is different
#             newStr += str((count)) + " " + last + " "
#             count = 1
#             last = char
#
#     newStr += str((count)) + " " + last
#
#     print(newStr)


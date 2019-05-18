#find all numbers divisible by 7 but NOT a multiple of 5 between n and n^


empty_list = []

for i in range(2000,4000):
    if (i%7 == 0) and (i%5 != 0):
        empty_list.append(int(i))

print(empty_list)


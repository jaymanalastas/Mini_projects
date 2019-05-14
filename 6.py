# for d in Y
#create a cool calculator
#find D

c = 50
h = 30

# use this formula Q = square root of [(2*c*d)/h]
#find d

import math
x = []
y = [i for i in input('give me a number: ').split(',')]
for d in y:
    x.append(str(int(round(math.sqrt((2*c*float(d))/h)))))
print(', '.join(x))


